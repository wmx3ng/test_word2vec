# -*- coding: utf-8 -*-

"""
@Time    : 9/11/17 5:16 PM
@Author  : wong
@E-Mail  : wmx3ng@gmail.com
@File    : exact_words.py
@Software: PyCharm
@Description: separator line to words. 1) upper to lower case. 2) convert punct to space. 3) separate line by space.
"""
import string


def sepatate_line(line):
    words = []
    if not line:
        return words

    line = line.lower()
    line = line.replace(string.punctuation, ' ')

    return line.split(' ')


if __name__ == '__main__':
    with open('../data/news/plain_news.example', 'r') as news_r:
        lines = news_r.readlines()
        for line in lines:
            print("--------------------")
            words = sepatate_line(line)
            print(words)
