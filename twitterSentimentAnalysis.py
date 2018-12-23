import tweepy # To access the twitter API
from textblob import TextBlob # Help us perform the actual sentiment analysis

# Authenticating with twitter require the following 4 variables
consumer_key = 'RI86ZtJHiQK8IHtxymRSMjPpV'
consumer_secret = '8H7DyPuT1Fgs9mGhRcnpEn84IJTapv4Lq2Ktk2RrmUjpBphkdv'
access_token = '741618670485528577-8tB7UY14vU8F7AFHYh2InefgERKIO6H'
access_token_secret = 'c4FfxRbEeWCh6Kki1cQtnDXfq1x5fHi6nFMCcA8xcGl1A'

# Use tweepy to authenticate to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Set up our API variable
api = tweepy.API(auth)

# We want to collect tweets that contain a certain keyword
# Create a public tweet variable to store a list of tweets
public_tweets = api.search('Trump')

# Print all the tweets that contain the previous keyword
for tweet in public_tweets:
	print(tweet.text) # Print the tweet
	analysis = TextBlob(tweet.text) # This will allow us to do experiments on text
	print(analysis.sentiment) # Get the sentiment from the tweet