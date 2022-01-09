# Environment Set Up

## Introduction

Now that all the softwares are installed and configured, it is possible to set up the environment of the system. The aim is to create the topics, database and install the Python packages that will be used to make the system work.

## Kafka Topic

We can first open a Git Bash window in the Kafka directory and execute the following commands for the creation of Kafka topics. Kafka topics are categories that allow organizing message streams. Each topic has a name that is unique and consumers or producers can connect to specific topics to obtain specific messages. In the case of this project, we need two topics.

- "tweets" that that will contain the raw data from Twitter
- "tweetsSentiment" that will contain the sentiment analysis attribute

