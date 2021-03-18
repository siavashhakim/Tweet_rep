import tweepy

consumer_key = "8aB5FdIMcDzCOdKpxCgMwaLsc"
consumer_secret = "Pmt5WVYRH4Sn0hTk6Y12uV1X6VSFBrErKHS4WODzjfW52zkJMa"

access_token = "1183977517301956609-ke4zLcpvOXZ1LF2LvD9TFKIEPgygib"
access_token_secret = "ZnICg26wCACeWyKTHAalLbCngkgWfieJ4mD5XLifz803k"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)




