# Visualizing Data

## Introduction

Similarly to Kafka and Twitter, we use the HBase software because NiFi provides the practical "PutHBaseJSON" component to connect to this particular software and send data to a given database. Indeed, to see the dataflow worked all the way through, we have a visual result by looking at the database that contains tweets and their sentiment analysis.

## Data sent by NiFi

Now, we can see how it works in our use case. As explained before, HBase allows us to easily check if the model has correctly given a sentiment to the tweet before sending it back to Kafka. Indeed, the tweet is only sent to HBase after being checked that the "sentiment" attribute in the JSON file is not empty. If that is the case, then we can see in the "tweets_sentiment" database that the tweets are correctly stored with the corresponding sentiment analysis.

We can have a look at the output data from the "PutHBaseJSON" component from NiFi. If the window is empty, it means the filtering from the previous component has spotted that the tweet had no sentiment attribute. In the following image we show a successful result where the data provenance is not empty.

![analysis](https://github.com/AmauryDM/twitter-dataflow/blob/main/images/analysis.png)

Each line represents a tweet that can be sent to HBase because a positive or negative sentiment has been attributed to the corresponding text. It is also possible to check it with the information button at the far left and clicking the "View" button of "Output Claim".

![sentiment](https://github.com/AmauryDM/twitter-dataflow/blob/main/images/sentiment.png)

In this project, the attributes that are kept in the database for better readability are: id, text, sentiment and time stamp. It is possible to modify the attributes that can be stored in the database by modifying the properties of the "AttributesToJSON" component. To do so, double click on the component, go to the "PROPERTIES" tab and add modify the attributes list.

## Final result in HBase

To check the result in HBase, go to the `hbase shell` window that is opened from the creation of the database and execute the following command.
~~~
scan 'tweets_sentiment'
~~~

If "AcquireTwitterData", "StreamTweetsToHBase" are launched and the Python script is running, we can obtain the following results in the database.

![scan](https://github.com/AmauryDM/twitter-dataflow/blob/main/images/scan.png)

As we can see, we have the row and the different columns that contain the data from NiFi. The visible data are the text, the sentiment and the id of the tweet. We have finally put in place the data flow of tweets from Twitter to HBase and perform sentiment analysis to the text of those tweets.
