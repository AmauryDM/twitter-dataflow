# Environment Set Up

## Introduction

Now that all the softwares are installed and configured, it is possible to set up the environment of the system. The aim is to create the topics, database and install the Python packages that will be used to make the system work.

## Kafka Topic

We can first open a Git Bash window in the Kafka directory and execute the following commands for the creation of Kafka topics. Kafka topics are categories that allow organizing message streams. Each topic has a name that is unique and consumers or producers can connect to specific topics to obtain specific messages. In the case of this project, we need two topics.

- "tweets" that that will contain the raw data from Twitter
- "tweetsSentiment" that will contain the sentiment analysis attribute

To create the "tweets" topic
~~~
bin/kafka-topics.sh --create --zookeeper localhost:2888 --replication-factor 1 --partitions 10 --topic tweets
~~~

To create the "tweetsSentiment" topic
~~~
bin/kafka-topics.sh --create --zookeeper localhost:2888 --replication-factor 1 --partitions 10 --topic tweetsSentiment
~~~

## HBase Table

Then, the goal is to create the database that will store the analyzed tweets. To do so, with HBase running, open a Command Prompt in the `.\bin\` folder and type this line that will open the builtin HBase interpreter. 
~~~
hbase shell
~~~

Type the following command that will create the database with its corresponding key.
~~~
create 'tweets_sentiment', 'social_media_sentiment'
~~~

## Python Libraries

Finally, we need to install the Python libraries used by the script in order to perform sentiment analysis on the tweets with the Deep Learning model developed. If Python is well installed with the environment variable set, the installation of the required libraries consists in the following commands.
~~~
pip install numpy
pip install confluent-kafka
pip install tensorflow
pip install transformers
~~~

With these installations, the development environment is set up. Now, we have all the elements to put in place the dataflow and make everything work.
