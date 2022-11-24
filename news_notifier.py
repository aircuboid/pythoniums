# Python program to illustrate 
# desktop news notifier
import os
import time

import feedparser
import notify2


def parseFeed():
    f = feedparser.parse("http://rss.cnn.com/services/podcasting/cnn10/rss.xml")
    breakpoint()
    ICON_PATH = os.getcwd() + "/icon.ico"
    notify2.init('News Notify')
    for newsitem in f['items']: 
        n = notify2.Notification(newsitem['title'], 
                                 newsitem['summary'], 
                                 icon=ICON_PATH 
                                 )
    n.set_urgency(notify2.URGENCY_NORMAL)
    n.show()
    n.set_timeout(15000)  # In seconds
    time.sleep(1200)  # In seconds
      
if __name__ == '__main__':
    parseFeed()
