from confluent_kafka import Consumer, Producer, SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from time import sleep
import json
import re
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import AutoTokenizer

broker = "localhost:9092"
topic_consumer = "tweets"
topic_producer = 'tweetsSentiment'
group_id = "3"

consumer_config = {'bootstrap.servers': broker,
				   'group.id': group_id,
				   'auto.offset.reset': 'largest',
				   'enable.auto.commit': 'false',
				   'max.poll.interval.ms': '86400000'}

producer_config = {'bootstrap.servers': broker,
				   'socket.timeout.ms': 100,
				   'api.version.request': 'false',
				   'broker.version.fallback': '0.9.0'}

consumer = Consumer(consumer_config)
consumer.subscribe([topic_consumer])

producer = Producer(producer_config)

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print("Message delivery failed: {}".format(err))
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))

def send_msg_async(msg):
    print("Send tweet sentiment asynchronously")
    producer.produce(topic_producer,
    				 msg,
    				 callback=lambda err,
    				 original_msg=msg: delivery_report(err, original_msg))
    producer.flush()

try:
    print("Loading tokenizer")
    tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
    print("Tokenizer loaded")
    print("")
    print("Loading model")
    model = tf.keras.models.load_model('model_emb256_dp4_lstm128_v4.h5')
    model.summary()
    print("Model loaded")
    print("")
    while True:
        print("Listening")
        msg = consumer.poll(0)

        if msg is None:
            sleep(5)
            continue
        if msg.error():
            print("Error reading message : {}".format(msg.error()))
            continue

        tweetSentiment = json.loads(msg.value().decode('utf8'))
        remove_rt = lambda x: re.sub('RT @\w+: '," ",x)
        remove_poll = lambda x: re.sub('POLL: '," ",x)
        rt = lambda x: re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x)

        if tweetSentiment['lang'] == 'en':
            text = rt(remove_poll(remove_rt(tweetSentiment['text']))).lower()
            tweetSentiment.update({'text':text})
            print(tweetSentiment['text'])

            tokenized_text = tokenizer(tweetSentiment['text'], return_tensors="np")
            text = pad_sequences(tokenized_text['input_ids'], maxlen=200)
            # text = np.expand_dims(padded_sequence, axis=0)
            prediction = model.predict(text).round().item()
            if prediction > 0.0:
                tweetSentiment.update({'sentiment':'positive'})
            else:
                tweetSentiment.update({'sentiment':'negative'})

            print(tweetSentiment['sentiment'])
            send_msg_async(json.dumps(tweetSentiment))
            consumer.commit()

except Exception as ex:
    print("Kafka Exception : {}".format(ex))

finally:
    print("Closing consumer")
    consumer.close()
