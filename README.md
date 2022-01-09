# Sentiment Analysis On Twitter Dataflow

## Introduction

This project aims at setting up an application of Big Data from start to end. It is inspired by a [Hortonworks Tutorial](https://github.com/hortonworks/data-tutorials/blob/master/tutorials/cda/building-a-sentiment-analysis-application/tutorial-0.md) for Data Engineers and Data Scientist to use multiple Big Data technologies provided by Apache. The final application is a Real-Time Sentiment Analysis Application installed on a Windows 10 machine. The application acquires real-time data generated on the Twitter feed via the API, filters it to pass it through a Deep Learning sentilent analysis model and finally stores the analyzed data into a database. More information can be found on the original tutorial that is adapted here in order to bypass the use of the Hortonworks Sandbox. 

## Big Data technologies used

This is a list of the technologies that are involved in the application with the version used and the link to the installation kit.

- [Twitter API v1.1](https://developer.twitter.com/en): Programmatic access to Twitter
- [Python 3.8.5](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe): Interpreted high-level general-purpose programming language
- [Apache NiFi](https://archive.apache.org/dist/nifi/1.14.0/nifi-1.14.0-bin.zip): Software project to automate the flow of data between software systems
- [Apache Kafka 2.4.1 - Scala 2.11](https://archive.apache.org/dist/kafka/2.4.1/kafka_2.11-2.4.1.tgz): Distributed event streaming platform for handling real-time data feeds
- [Apache Hadoop 3.1.0 - HDFS](https://archive.apache.org/dist/hadoop/common/hadoop-3.1.0/hadoop-3.1.0.tar.gz): Distributed file-system that stores data on commodity machines
- [Apache HBase 2.2.5](https://archive.apache.org/dist/hbase/2.2.5/hbase-2.2.5-bin.tar.gz): Non-relational distributed database

The Twitter API is the exception that requires to sign up to the Elevated access. Indeed, the NiFi software in charge of generating the dataflow uses the v1.1 endpoint that only comes with this particular access.

## Objectives

- Create a Twitter Application using Twitter's Developer Portal to get KEYS and TOKENS for connecting to Twitter API v1.1 endpoint
- Create a NiFi Dataflow Application that integrates Twitter's Decahose API to ingest tweets, perform preprocessing and store the data into a Kafka Topic "tweets"
- Install a Python Deep Learning algorithm for Natural Language Processing to classify text tweets in Positive/Negative and store the analyzed data into another Kafka Topic "tweetsSentiment"
- Create a NiFi Dataflow Application that ingests the Kafka Topic "tweetsSentiment" to stream analyzed tweets data to a database
- Visualize the tweet sentiments in a "tweets_sentiment" HBase table

## Prerequisites

- JDK 8 is installed and the JAVA_HOME path variable is set (no spaces in the path recommended)
- Administrator rights on the machine
- Project installed in the directory "C:/twitter/", changes may occur if the path is not exactly the same

## Tutorial sequence

The README serves as an introduction to the project. In order to follow the installation and configuration of the application, one is invited to go through the different text files explaining step by step how to put it in place. This tutorial sequence contains the following modules:

1. **Configuration of the softwares**: Properly install the listed softwares and modify the configuration files
2. **Setting up the environment**: Create the Kafka topics, the HBase table and install the Python libraries to run the script
3. **Data pre-processing**: Install the NiFi dataflow using the XML file and modify the Twitter connector with KEYS and TOKENS
4. **Sentiment analysis**: Launch the Python script to connect to the Kafka topics and analyze the tweets
5. **Data post-processing**: Filter the data sended back by the Python script and store it to the HBase table
6. **Visualizing analyzed data**: Scan the HBase table to see the sentiment results
