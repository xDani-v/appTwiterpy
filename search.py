import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

client = tweepy.Client(
    consumer_key=config.API_KEY, consumer_secret=config.API_SECRET,
    access_token=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_TOKEN_SECRET
)

print(client)

response = client.search_recent_tweets("Tweepy")
# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

# Each Tweet object has default ID and text fields
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)

# By default, this endpoint/method returns 10 results
# You can retrieve up to 100 Tweets by specifying max_results
response = client.search_recent_tweets("Tweepy", max_results=100)
