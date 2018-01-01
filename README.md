# Gaccho Twitter

Plug-in to receive Twitter timeline at [gaccho](https://github.com/nobiki/gaccho)

## Setup

Setting of "gaccho.ini"

#### [Account] Section.

* [Account] (required)  
First time OAuth authentication is required.  
The account name displayed in the list.  
"Account" is an arbitrary character string set with 8 bytes  
Common setting of `type = Twitter` is set in the [Twitter] section

* type (required)  
Set "Twitter".

* color_text (optional): [default](https://github.com/nobiki/gaccho_twitter/blob/0.1/gaccho_twitter/Twitter.py#L37)
* color_back (optional): [default](https://github.com/nobiki/gaccho_twitter/blob/0.1/gaccho_twitter/Twitter.py#L37)

* feeds (optional)  
Set feeds to subscribe by line break separator.

```
[Account1]
type = Twitter

color_text = [BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]
color_back = [BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE]

[Account2]
type = Twitter

    :

```

#### [Twitter] Section

* [Twitter] (required)  
Common setting concerning "type = Twitter"

* interval (required):  
Set the retention period of the local cache in minutes. (default: 60 minutes)

* CONSUMER_KEY and CONSUMER_SECRET (required):  
You need consumer_key and consumer_secret issued from Twitter.  
That's based on Twitter's API Terms of Service.

* count (optional):  
The number of tweets requested from the API. (Recommended: 100)  
That's based on Twitter's API Terms of Service.

```
[Twitter]
interval = 5

CONSUMER_KEY = xxxxxxxxxx
CONSUMER_SECRET = xxxxxxxxxx

count = 100
```
