import tweepy
import json
import urllib2
import datetime
today = datetime.date.today()

consumerKey = "LC7Tx9Aq52HL74SxqTeyIgstF"
consumerSecret = "kgDLUdJwiQiI0p1o0Ipk1HdpWGz5DEKvYMkKojnTgnLYQyREQL"
accessToken = "883952400-SIfp9AKEOhBH9i5m9z5nf2eatM9G3L1gD4E719DF"
accessTokenSecret = "sWzXhljGRpOGpUKVB0yODR4LWEdAwwtdEkjeSRpb0FwjQ"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

results = api.trends_place(23424934)

trends = []
count = 0
for location in results:
	for trend in location["trends"]:
		count +=1
		trending = str(count)+". "+trend["name"]
		trends.append(trending)
		#print " - %s" % trend["name"]

trending = trends[:10]

payload={"username": "TOP 10 Trending in PH (Michael Gonzales)", "text":"Trending today: {:%B %d, %Y}".format(today)+"\n"+"\n".join(trending)}
#payload={"username": "TOP 10 Trending in PH", "text":"Trending today: {:%B %d, %Y}".format(today)+" | As of: 8:00 AM (GMT+8)"+"\n"+"\n".join(trending)}
#payload ={"title": "TRENDing in PH","text": "\n".join(FinTrendList),"mrkdwn_in": ["text",]}
req = urllib2.Request('https://hooks.slack.com/services/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')
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(payload))
#print " - %s" % trend["name"]
print "DONE!"