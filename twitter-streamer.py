from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from credentials import  twitter_credentials


class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self,status):
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credentials.consumerKey, twitter_credentials.consumerSecret)
    auth.set_access_token(twitter_credentials.accessKey,twitter_credentials.accessSecret)

    stream = Stream(auth, listener)

    stream.filter(track=['bbb','corona','covid'])


