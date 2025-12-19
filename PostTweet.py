#coding:utf-8
import config
import tweepy

# Accesss Token Secert
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

try:
    api.update_status("久々にpythonからTwitterいじってる。\n，pythonからテストポストっすよ。")
    print("トゥイ―トしました(*‘ω‘ *)")
except:
    print("失敗したみたいです(/ω＼)")