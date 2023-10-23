import snscrape.modules.twitter as sntwitter
from cleantext import clean
import re

istenen = ["lmfao", "lit", "lol", "w8","btw"]
istenmeyen = ["therefore","assessment","definition","distribution"]
all_tweets=[]
limit=50

istenmeyen_kelime=""
for a in istenmeyen:
    istenmeyen_kelime = istenmeyen_kelime + " -" + a

for a in istenen:
    query = a + istenmeyen_kelime + " lang:en"
    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        if len(tweets) == limit:
            all_tweets.append(tweets)
            break
        else:
            tweets.append([tweet.content])

d = 1
with open('tweets.txt', 'w') as f:
    for a in all_tweets:
        for e in a:
            for b in e:
                c = clean(b, no_emoji=True)

                c = re.sub('http://\S+|https://\S+', '',c)
                c = re.sub('@\S+', '', c)
                c = re.sub('\n', '', c)

                f.write(c)   
                f.write('\n')
                d = d + 1