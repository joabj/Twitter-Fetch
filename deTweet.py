#This program will take a Twitter user timeline, as returned by the Twitter API (from the Fetch.py program), and format
#the text, time, location, and Tweet ID. In this case for printing onto the screen, but can be piped elsewhere.
#Eventually optional attributes, such as a photos, will also be included. 
#
#Running from the command line, the program needs the name of the .json file where the timeline has been stored (by Fetch.py
#in my own setup) i.e. "deTweet.py 170602.json")
#
#Also, this program captues, and writes to a text file the ID of the last Tweet, which will be useful for fetching new data only
#since the last date. This may be moved somewhere else eventually.
 

import sys
import json


tweetFile = str(sys.argv[1])

#Create an HTML file
HTMLFilePrep = tweetFile.split('.')
HTMLFile = HTMLFilePrep[0]+".html"
target = open(HTMLFile, 'w')

data = json.load(open(tweetFile))
tweetCount = len(data)
i = 0

while i < len(data):
	tweetNumber = data[i]["id"]
	tweet = data[i]["text"]
	tweetLocale = data[i]["coordinates"]
	tweetTime = data[i]["created_at"]
	target.write(tweet.encode('utf-8'))
	target.write("<p>")	
	target.write(str(tweetNumber))
	target.write("<p>")	
	target.write(str(tweetLocale))
	target.write("<p>")	
	target.write(str(tweetTime))
	target.write ("</p>")
	target.write("<p>")	
	i = i + 1
	
	
	
#Close the file:
target.write("</table></center>")	
target.write("<img id=ImageCenter src=/Tilde-Color.jpg  height=27 width=60><p>")	
target.close()

#Capture the ID of the last Tweet 
LastTweet = str(data[0]["id"])
f = open("LastTweet.txt", 'w')
f.write(LastTweet)
f.close()



#http://www.pythonforbeginners.com/system/python-sys-argv
