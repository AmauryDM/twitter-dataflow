# Sentiment Analysis On Twitter Dataflow

## Introduction

This project aims at setting up an application of Big Data from start to end. It is inspired by [Hortonworks Tutorial](https://github.com/hortonworks/data-tutorials/blob/master/tutorials/cda/building-a-sentiment-analysis-application/tutorial-0.md) to for Data Engineers and Data Scientist to use multiple Big Data technologies provided by Apache. The final application is a Real-Time Sentiment Analysis Application installed on a Windows 10 machine. The application acquires real-time data generated on the Twitter feed via the API, filters it to pass it through a Deep Learning sentilent analysis model and finally stores the analyzed data into a database. More information can be found on the original tutorial that is adapted here in order to bypass the use of the Hortonworks Sandbox. 

### Big Data technologies used

This is a list of the technologies that are involved in the application with the version used and the link to the installation kit.

- [Twitter API v1.1](https://developer.twitter.com/en)
- [Python 3.8.5](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)
- [Apache NiFi](https://archive.apache.org/dist/nifi/1.14.0/nifi-1.14.0-bin.zip): Software project to automate the flow of data between software systems
- [Apache Kafka 2.4.1 - Scala 2.11](https://archive.apache.org/dist/kafka/2.4.1/kafka_2.11-2.4.1.tgz): Distributed event streaming platform for handling real-time data feeds
- [Apache Hadoop 3.1.0 - HDFS](https://archive.apache.org/dist/hadoop/common/hadoop-3.1.0/hadoop-3.1.0.tar.gz): Distributed file-system that stores data on commodity machines
- [Apache HBase 2.2.5](https://archive.apache.org/dist/hbase/2.2.5/hbase-2.2.5-bin.tar.gz): Non-relational distributed database

The Twitter API is the exception that requires to sign up to the Elevated access. Indeed, the 
