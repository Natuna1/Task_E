"""
トップページに表示されているニュースのタイトルおよびリンクURLを取得してください
title 
url
"""
import requests
import time


def top_articles():
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')  # 新しいトップ記事

    dic = response.json()  # パース

    numbers = []
    for number in range(0, 50):
        numbers.append(dic[number])

        return numbers

"""
def get_information(number):
    for x in numbers:
        search_number = x
        response = requests.get(f'https://hacker-news.firebaseio.com/v0/{search_number}.json?print=pretty')
"""


def main():
    numbers = top_articles()
    print(numbers)
    # get_info(numbers)


if __name__ == "__main__":
    main()