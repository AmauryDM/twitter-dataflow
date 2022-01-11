# Sentiment Analysis

## Introduction

In this part, the aim is to present the Python code used in order to perform sentiment analysis on real time data consumed in the "tweets" topic. Afterwards, this data will be produced in the "tweetsSentiment" topic and consumed back by NiFi now that it has the newly updated "sentiment" attribute.

We use the Confluent Python library in order to connect to Kafka using a Python script. Indeed, Confluent provides high-level reliable and performant producer and consumer. Consumers are simply the client applications, in that case the Confluent class, that subscribe to a topic in order to read and process the events like the Twitter data.

## Code review

The script [`twitter.py`](https://github.com/AmauryDM/twitter-dataflow/blob/main/files/twitter.py) and the file [`model model_emb256_dp4_lstm128_v3.h5`](https://github.com/AmauryDM/twitter-dataflow/blob/main/files/model_emb256_dp4_lstm128_v3.h5) are available in the [`files/`](https://github.com/AmauryDM/twitter-dataflow/tree/main/files) folder of the repository. Thus, the script can be explained as follows. We first create a consumer for the "tweets" topic and a producer for the "tweetsSentiment" topic thanks to the information provided by Kafka.

Then, the steps are executed:
- The tokenizer used for the Deep Learning model is loaded
- The model is loaded
- An infinite loop is initiated to listen to the messages sent to the "tweets" topic and when a message is received
  - The consumer loads the message and the script cleans it from unwanted string of characters such as "RT" when it is a retweet or "@" when someone is mentioned
  - It verifies the message language is correctly labeled as English
  - It performs the prediction on the text
  - It adds a new attribute "sentiment" to the JSON that was loaded with the result of the analysis either Positive or Negative
  - The producer sends the message asynchronously to the "tweetsSentiment" topic in Kafka via the producer

## Code execution

Finally, to launch the script, open a command prompt window in the directory with the Python files and execute the following command.
~~~
python twitter.py
~~~

When launched for the first time, the window will look like the following image. Indeed, the tokenizer is downloaded from the Hugging Face archives and installed locally. This action will not be reproduced for the next executions.

![execution](https://github.com/AmauryDM/twitter-dataflow/blob/main/images/execution.png)

Then, we can see the summary of the Deep Learning model that was used. It shows that the file was successfully loaded and can be used for sentiment analysis. After that, the message "Listening" appears showing that Python has connected the consumer to the "tweets" topic and waits for the messages from NiFi.

In the next images, we can see that messages are received by the Python consumer and analyzed by the model. Thus, the following pieces of information are displayed: the text of the tweet, the sentiment associated and the message saying the new JSON file has been successfully sent to the "tweetsSentiment" topic.

![listening](https://github.com/AmauryDM/twitter-dataflow/blob/main/images/listening.png)

After that, NiFi connects to the "tweetsSentiment" topic as a consumer with a corresponding component in order to retrieve the analyzed tweet from the Deep Learning model.
