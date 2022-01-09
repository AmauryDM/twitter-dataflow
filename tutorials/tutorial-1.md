# Software Configuration

## Introduction

The first goal is to install all the required softwares and modify the configuration files in order to launch the whole system successfully. As presented in the README, the focus is on the following softwares. One has to apply for Elevated access on the Twitter Developer Platform to gain access to v1.1 endpoint.

- [Python 3.8.5](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)
- [Apache NiFi](https://archive.apache.org/dist/nifi/1.14.0/nifi-1.14.0-bin.zip)
- [Apache Kafka 2.4.1 - Scala 2.11](https://archive.apache.org/dist/kafka/2.4.1/kafka_2.11-2.4.1.tgz)
- [Apache Hadoop 3.1.0 - HDFS](https://archive.apache.org/dist/hadoop/common/hadoop-3.1.0/hadoop-3.1.0.tar.gz)
- [Apache HBase 2.2.5](https://archive.apache.org/dist/hbase/2.2.5/hbase-2.2.5-bin.tar.gz)

The project is built for Windows 10 machine. That is, once the Python executable file is downloaded, make sure it is added to the Path environement variable. If the installation is successful, open a Command Prompt window and execute the line to display the Python version.

~~~
python --version
~~~
