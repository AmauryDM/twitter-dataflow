# Visualizing Data

## Introduction

Similarly to Kafka and Twitter, we use the HBase software because NiFi provides the practical "PutHBaseJSON" component to connect to this particular software and send data to a given database. Indeed, to see the dataflow worked all the way through, we have a visual result by looking at the database that contains tweets and their sentiment analysis.

## Data sent by NiFi

Now, we can see how it works in our use case. As explained before, HBase allows us to easily check if the model has correctly given a sentiment to the tweet before sending it back to Kafka. Indeed, the tweet is only sent to HBase after being checked that the "sentiment" attribute in the JSON file is not empty. If that is the case, then we can see in the "tweets_sentiment" database that the tweets are correctly stored with the corresponding sentiment analysis.

We can have a look at the output data from the "PutHBaseJSON" component from NiFi. If the window is empty, it means the filtering from the previous component has spotted that the tweet had no sentiment attribute. In the following image we show a successful result where the data provenance is not empty.
