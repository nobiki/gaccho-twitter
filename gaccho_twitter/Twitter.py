from Article import Article

import os
import time
import configparser

from twitter import *

# load config
config = configparser.ConfigParser()
config.read("gaccho.ini")
conf = dict(config["Twitter"])

if "consumer_key" in conf and "consumer_secret" in conf:
    CONSUMER_KEY        = str(conf["consumer_key"])
    CONSUMER_SECRET     = str(conf["consumer_secret"])

# twitter oauth
tw = {}
for c in enumerate(config):
    if "type" in config[c[1]] and "Twitter" == config[c[1]]["type"]:
        item = c[1]
        account = dict(config[item])

        ACCOUNT_CREDS = "cache/.twitter_"+item+"_credentials"

        if not os.path.exists(ACCOUNT_CREDS):
            print("[gaccho_twitter] Please authenticate account @"+item)
            oauth = oauth_dance("gaccho",CONSUMER_KEY, CONSUMER_SECRET, ACCOUNT_CREDS)

        OAUTH_TOKEN, OAUTH_SECRET = read_token_file(ACCOUNT_CREDS)
        tw[item] = Twitter( auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET) )

class Twitter(Article):

    def color_pair(self):
        return {"color_text":"BLACK", "color_back":"CYAN"}

    def get(self):
        ret = []
        for account in tw:
            if "count" in conf:
                home = tw[account].statuses.home_timeline(count=conf["count"])
            else:
                home = tw[account].statuses.home_timeline()

            for line in home:
                name = "@"+line["user"]["screen_name"]
                published = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(line["created_at"],'%a %b %d %H:%M:%S +0000 %Y'))
                author = "@"+line["user"]["screen_name"]
                title = line["user"]["name"]+": "+line["text"].replace("\n","")
                value = line["text"]
                link = "https://twitter.com/"+line["user"]["screen_name"]+"/status/"+line["id_str"]
                ret.append((account, name, str(published), author, title, link, value))

        self.cache_save("cache/Twitter", ret)

        return ret

    def controll(self, **keywords):
        ret = {"key_trigger":"","key_pair":""}

        ## tweet tw
        elif keywords["key_pair"] == ord("t") and keywords["key"] == ord("w"):
            ret["key_trigger"] = "tweet"
            keywords["key_pair"] = ""

        ## re tweet tr
        elif keywords["key_pair"] == ord("t") and keywords["key"] == ord("r"):
            ret["key_trigger"] = "retweet"
            keywords["key_pair"] = ""

        ## del tweet td
        elif keywords["key_pair"] == ord("t") and keywords["key"] == ord("d"):
            ret["key_trigger"] = "del tweet"
            keywords["key_pair"] = ""

        ## fav tweet tf
        elif keywords["key_pair"] == ord("t") and keywords["key"] == ord("f"):
            ret["key_trigger"] = "fav tweet"
            keywords["key_pair"] = ""

        return ret
