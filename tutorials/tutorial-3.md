# Data Pre-processing

## Introduction

In this part, we explain how NiFi works, why it is used and how we use it in the case of Twitter to obtain this real time data. Indeed, NiFi proposes a component that is directly configured to connect to Twitter API and pull tweets from the real time feed. That is why we are studying this particular use case when using NiFi.

## Install NiFi dataflow

In order to install the whole dataflow configured and used for this project, we can use the `flow.xml` file contained in the `files/` folder in the repository of the project. All that needs to be done is right click in the NiFi canva and type "Upload template" to select the file.

The canva should look as represented in the following image with the two groups used for the project. The groups are divided as follows:
- AcquireTwitterData for pre-processing
- StreamTweetsToHBase for post-processing

![groups](https://github.com/AmauryDM/twitter-dataflow/blob/main/images/groups.png)

We will first focus on the pre-processing group and go through the components that are used for this project. It is possible to view them by clicking on the group. We obtain the following components on the canvas.

| Component | Operation |
| --- | --- |
| GetTwitter | Connect to Twitter API v1.1 endpoint |
| PullKeyAttributes | Filter on given attributes in the JSON file of the tweet |
| FindOnlyTweets | Filter tweets that have a text attribute not empty |
| PublishKafka | Connect as producer to the "tweets" topic in Kafka |
