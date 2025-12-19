import tweepy
import config

 # TwitterAPIの認証データを取得して認証
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, ATS)

api = tweepy.API(auth, wait_on_rate_limit = True)

print('タイムライン漁ってきまーす( ੭˙꒳ ˙)੭')

 #つぶやきを格納するリスト
tweetsList = []
tweets = api.home_timeline(count=100)

for tweet in tweets:
     #ツイートテキストをリストに追加
    tweetsList.append(tweet.text + '\n')

    #ファイル出力
    with open('D:\python\Timeline.txt',"w",encoding="utf-8") as f:
        f.writelines(tweetsList)

print('完了だぜgj')