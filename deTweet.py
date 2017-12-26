#This program will take a Twitter user timeline, as returned by the Twitter API (from the Fetch.py program), and format
#the text, time, location, and Tweet ID. In this case for printing onto the screen, but can be piped elsewhere.
#Eventually optional attributes, such as a photos, will also be included. 
#
#Also, this program captues, and writes to a text file the ID of the last Tweet, which will be useful for fetching new data only
#since the last date. 
 


import json
data = json.load(open('NAME-OF-TWEET-FILE.json'))
tweetCount = len(data)
i = 0

while i < len(data):
	tweetNumber = data[i]["id"]
	tweet = data[i]["text"]
	tweetLocale = data[i]["coordinates"]
	tweetTime = data[i]["created_at"]
	print tweet
	print tweetNumber
	print tweetLocale
	print tweetTime
	print "  "
	i = i + 1

#Capture the ID of the last Tweet 
LastTweet = str(data[0]["id"])
f = open("LastTweet.txt", 'w')
f.write(LastTweet)
f.close()
