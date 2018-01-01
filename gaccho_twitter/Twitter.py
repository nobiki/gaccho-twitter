from Article import Article

import os
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
        ## load config
        self.config = configparser.ConfigParser()
        self.config.read("gaccho.ini")

        ret = []
        for account in tw:
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
