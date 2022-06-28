"""
トップページに表示されているニュースのタイトルおよびリンクURLを取得してください
title 
url
"""
import requests
import time


def Top_Articles():
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')  # 新しいトップ記事

    dic = response.json()  # 辞書として表示...パース
    print(dic)
# typeを使ってjsonを調べる
  #  print(type(response.json()))
  #  number = []
    for number in range(0, 50):
        print(number)
        time.sleep(1)  # ここで1秒止まる

  # def News():
  # response = requests.get(f'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')  # 新しいトップ記事
