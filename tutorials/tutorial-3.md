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

The only component that requires modification is the first: "GetTwitter". Indeed, it has to be adapted to the Twitter project linked. We have the properties presented in this image.

![properties](https://github.com/AmauryDM/twitter-dataflow/blob/main/images/properties.png)

The first property allows us to specify that the data which will be queried from Twitter is a random sample of the real time Twitter feed. Then, we need to specify the different keys from the Twitter developer account. Indeed, to connect to Twitter, we need a project from the developer account that gives Consumer Key, Consumer Secret, Access Token and Access Token Secret. After that, the configuration of the pre-processing group is done. 

To launch the whole group, go back to the NiFi canvas by clicking on NiFi Flow at the bottom left corner. Then click on "AcquireTwitterData" and press the play button on the left "Operate panel". The red stop button will turn to a green play button meaning the data flow is launched. At this stage, Twitter is queried and data is retrieved, filtered and directly sent to the Kafka topic.

This is how we arrive now to the use of Kafka as a message manager. In fact, now the tweets are sent to the "tweets" Kafka topic. In order to process and perform complex operations on real time data, Kafka will help us to treat messages asynchronously.

At any time in the NiFi process, it is possible to view the data that is passing through the pipeline. To do so, right click on any component and select "View data provenance". Then choose a line of data and click on the far right information button that will open a pop-up window. Select the "CONTENT" tab and ‘View’ on the Output Claim. Here is an example of data from the "PublishKafka" component.

![output](https://github.com/AmauryDM/twitter-dataflow/blob/main/images/output.png)
