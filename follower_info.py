#coding:utf-8
import config
import tweepy
import time
import pandas as pd
from tqdm import tqdm

# Accesss Token Secert
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)
api = tweepy.API(auth)

my_user_id = "haida_ito" #ここに自分のuseridを入れる
follower_ids = api.followers_ids(my_user_id) #自分のアカウントのフォロワーをすべて取得する

follower_list = []
for follower_id in follower_ids:
    follower_list.append(follower_id)

print("あなたのフォロワーは" + str(len(follower_list)) + "人です。")

df = pd.DataFrame()

for follower in tqdm(follower_list):
    user =  api.get_user(follower)
    user_id         = user.screen_name     #ユーザー名
    description     = user.description     #プロフィール文
    tweet_count     = user.statuses_count  #ツイート数
    follower_count  = user.followers_count #フォロワー数
    following_count = user.friends_count   #フォロー数
    created_at      = user.created_at      #アカウント作成日
    protected       = user.protected       #鍵付きかどうか

    data = pd.Series([user_id,
                      description,
                      tweet_count,
                      follower_count,
                      following_count,
                      created_at,
                      protected])
    df = df.append(data, ignore_index=True)
    time.sleep(.26) #15分間で900ユーザー分のデータしか取得できないので、簡易的にスリープして対応

df.columns = ['user_id',
              'description',
              'tweet_count',
              'follower_count',
              'following_count',
              'created_at',
              'protected']

df.head()
