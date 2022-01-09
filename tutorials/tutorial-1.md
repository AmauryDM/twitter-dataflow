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

Then, all the archive files can be downloaded and extracted in the `C:\twitter\` directory. To simplify the course of the tutorial, each software folder should not contain another folder but directly the useful files (bin folder is the first for example). With the installation done, it is possible to move on to the configuration.

## NiFi

When installed and extracted, NiFi can be directly run from the `C:\twitter\nifi-1.14.0\bin` directory by launching a Command Prompt window and executing the `run-nifi.bat` file. After that go to https://127.0.0.1:8443/nifi on a web browser. It should request for a username and password that can be found in the `.\logs\nifi-app.txt` file by searching for "generated username".

## Kafka

Kafka needs to create a `C:\twitter\kafka_2.11-2.4.1\data\` folder containing a `kafka\` and a `zookeeper\` folder and apply the following modifications to the configuration files.

In `.\config\zookeeper.properties`
~~~
dataDir=C:/twitter/kafka_2.11-2.4.1/data/zookeeper
clientPort=2888
~~~

In `.\config\server.properties`
~~~
log.dirs=C:/twitter/kafka_2.11-2.4.1/data/kafka
~~~

To launch Zookeeper and Kafka, open two Git Bash windows in `C:\twitter\kafka_2.11-2.4.1\`. 

In the first execute
~~~
bin/zookeeper-server-start.sh config/zookeeper.properties
~~~

In the second execute
~~~
bin/kafka-server-start.sh config/server.properties
~~~

Zookeeper is a server for highly reliable distributed coordination of applications to be able for Kafka to manage different feeds of data which is the case in the project.

## Hadoop

The HADOOP_HOME environment variable should be set to point to `C:\twitter\hadoop-3.1.0` and added with `bin\` to the Path and the HADOOP_CONF_DIR variable set to `C:\twitter\hadoop-3.1.0\etc\hadoop`. Create in the directory a `data\` folder containing a datanode and a namenode folder. Then apply the following modifications to the configuration files in `.\etc\hadoop\`.

In `core-site.xml`
~~~
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>
~~~

In `mapred-site.xml`
~~~
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
~~~

In `hdfs-site.xml`
~~~
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>C:\twitter\hadoop-3.1.0\data\namenode</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>C:\twitter\hadoop-3.1.0\data\datanode</value>
  </property>
</configuration>
~~~

In `yarn-site.xml`
~~~
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
  <property>
    <name>yarn.nodemanager.auxservices.mapreduce.shuffle.class</name>  
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
  </property>
</configuration>
~~~

To make Hadoop run on Windows, it needs other utilities. They can be downloaded at the following address for 3.1.0 https://github.com/s911415/apache-hadoop-3.1.0-winutils and replace the actual bin folder by deleting it or renaming it. The success of the installation can be verified by executing in a Command Prompt window.
~~~
hadoop version
~~~

In that case, first in a Command Prompt, execute the line.
~~~
hdfs namenode -format
~~~

Then in another window in the `C:\twitter\hadoop-3.1.0\sbin\` folder, execute the following command that will launch Hadoop. 
~~~
start-dfs.cmd
~~~

It is only used in order to run HBase that allows us to create a database for the project.


## HBase

