import tweepy

# Replace these values with your own Twitter API keys and tokens
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

def post_tweet(tweet_text):
    """
    Posts a tweet to Twitter.
    :param tweet_text: The text of the tweet to post.
    """
    # Authenticate to Twitter
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    
    # Post the tweet
    api.update_status(tweet_text)
    print("Tweet posted:", tweet_text)
    