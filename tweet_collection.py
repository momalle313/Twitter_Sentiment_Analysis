#!/usr/bin/python
import sys
import getopt
import datetime
import tweepy

### Michael O'Malley, Michael Burke
### Machine Learning
### Semster Project
### Twitter Scraper

# Define usage for user
def usage():
    print "Usage: " + str(sys.argv[0]) + " [-#] [-h] keyword"

# Stream Listener for Location problem
class StreamListener(tweepy.StreamListener):
		
	# Open output file to append to
	def __init__(self, keywords):
		self.now = datetime.datetime.now()
		self.output = open(self.now.strftime("%Y-%m-%d") + '_Tweets.txt', 'a+')
		self.output.write("Keywords: " + str(keywords))
		self.num = 0

	# When a status is found, record the necessary information
	def on_status(self, status):
		self.num += 1
		print "Hit: " + str(self.num)
		self.output.write(status.text.encode('utf 8').replace('\n','') + '\n\n')

	# Stop if an error occurs
	def on_error(self, status_code):
        	print "Error Code: " + str(status_code)
        	return False


# Run main script
if __name__ == "__main__":

	# Check proper usage
	try:
		opts, args = getopt.getopt(sys.argv[1:], "#h", ["hashtag", "help"])
	except getopt.GetoptError:
		usage()
		sys.exit(1)

	# Check through arguments
	hashtag = False
	for opt, arg in opts:
		if opt in ('-#', '--hashtag'):
			hashtag = True
		elif opt in ('-h', '--help'):
			usage()
			sys.exit(0)

	keywords = args
	if hashtag:
		for i in range(0, len(keywords)):
			keywords[i] = '#' + keywords[i]

	# Consumer keys and access token
	consumer_key = 'l6h9Z40w3SM3QdFrRWH2hKVoL'
	consumer_secret = 'tPB3xDHDTnr3FjgV2pRKnc4mMBQyviPWyVmLqgYU4WaBc9BVI0'
	access_token = '960373416892170240-omnMrJJ2NDSkSL4HTEMEqgQlpIPsjQw'
	access_token_secret = 'KXs1K4jgmSe5pWCCWEhNZxiUR7wEkeo9KxNrSfhG7bk8a'
	 
	# OAuth process
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	 
	# Interface creation
	api = tweepy.API(auth)

	# Produce Stream results
	stream = tweepy.streaming.Stream(auth, StreamListener(keywords))
	stream.filter(track=keywords)


