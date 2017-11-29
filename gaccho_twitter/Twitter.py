from Article import Article

import configparser

from twitter import *

class Twitter(Article):
    def color_pair(self):
        return {"color_text":"WHITE", "color_back":"RED"}

    def get(self):
        ret = []

        ## load config
        self.config = configparser.ConfigParser()
        self.config.read("gaccho.ini")
        conf = dict(self.config["Twitter"])

        if "CONSUMER_KEY" in conf and "CONSUMER_SECRET" in conf:
            CONSUMER_KEY        = conf["CONSUMER_KEY"]
            CONSUMER_SECRET     = conf["CONSUMER_SECRET"]

            if "OAUTH_TOKEN" in conf and "OAUTH_SECRET" in conf:
                OAUTH_TOKEN     = conf["OAUTH_TOKEN"]
                OAUTH_SECRET    = conf["OAUTH_SECRET"]
            else:
                oauth = oauth_dance("gaccho",conf["CONSUMER_KEY"], conf["CONSUMER_SECRET_KEY"])
                OAUTH_TOKEN     = oauth[0]
                OAUTH_SECRET    = oauth[1]

            t = Twitter( auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY) )

            home = t.statuses.home_timeline()

            for line in home:
                name = "@"+line["user"]["screen_name"]
                published = line["created_at"]
                author = line["user"]["screen_name"]
                title = line["text"]
                link = "https://twitter.com/"+line["user"]["screen_name"]+"/status/"+line["id_str"]
                ret.append(("Twitter", name, str(published), author, title, link, self.strip_tags(value)))

        self.cache_save("cache/Twitter", ret)

        return ret
