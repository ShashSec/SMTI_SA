#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "702899742238355456-WjCmwMKVOM4M2uiWEZWC44egYNtZQQq"
access_token_secret = "OGa1Itn68ayIIfbY1X4CT6oFsg8oYYr4HSH6TIr06pgJJ"
consumer_key = "sdAAPAYcarXruSnqZRtcDsDgG"
consumer_secret = "0VNDw91owl6NHjBZPghacJL79wLtor5jRjlT41cvDyH1FcyonO"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        decoded = json.loads(data)
        print (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keyword: 'python'
    stream.filter(track=['python'])
