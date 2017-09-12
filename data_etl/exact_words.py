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
import re

_r_punct = re.compile(r'[{}]+'.format(re.escape(string.punctuation)))


def sepatate_line(line):
    if not line:
        return list()

    line_2_lower = line.lower()
    line_no_punct = _r_punct.sub(' ', line_2_lower)

    return [w for w in line_no_punct.split(' ') if w]


if __name__ == '__main__':
    with open('../data/news/plain_news.example', 'r') as news_r:
        lines = news_r.readlines()
        for line in lines:
            print("--------------------")
            words = sepatate_line(line)
            print(words)
