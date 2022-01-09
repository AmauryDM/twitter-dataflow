# Data Post-processing

## Introduction

Now that we have data sent to the "tweetsSentiment" topic, we can retrieve it and perform post-processing before storing it into a database. To do so, refer to the "StreamTweetsToHBase" group in NiFi. This group will contain the operations to ensure we can store labeled data with the "sentiment" attribute.

## NiFi post-processing group

With the installation of the whole dataflow done in the [Tutorial 3](https://github.com/AmauryDM/twitter-dataflow/edit/main/tutorials/tutorial-3.md), we can have a look at this other group to explain how it works and what to modify depending on the needs. We have the following components and the operation associated.

| Component | Operation |
| --- | --- |
| ConsumerKafka | Retrieve the analyzed tweets in the "tweetsSentiment" topic |
| PullKeyAttributes | Filter on specific attributes especially "sentiment" |
| AttributesToJSON | Make sure the format of the file is JSON with the correct attributes |
| IfTweetsHaveSentimentAndTime | Filter tweets that have a time stamp and the attribute "sentiment’" not empty |
| PutHBaseJSON | Connect to the HBase client in the "tweets_sentiment" database created with the "social_media_sentiment" key associated |

In order to see the results, the group has to be launched from the NiFi canvas by selecting and pressing the play button on the "Operate panel". When the green play button appears, data from the "tweetsSentiment" topic is received and filtered then directly sent to HBase if the requirements are respected.

As always, we can have a look at the data that is running through the pipeline with the "View data provenance" option in the right click. In the following example from the "ConsumerKafka" component, we can see the JSON file retrieved from the "tweetsSentiment" topic. We can see that this file has indeed the new attribute "sentiment" that is set to positive for this particular tweet.

![consumer](https://github.com/AmauryDM/twitter-dataflow/blob/main/images/consumer.png)
