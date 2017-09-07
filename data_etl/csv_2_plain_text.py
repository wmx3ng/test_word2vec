# -*- coding: utf-8 -*-

"""
@Time    : 9/7/17 1:24 PM
@Author  : wong
@E-Mail  : wmx3ng@gmail.com
@File    : csv_2_plain_text.py
@Software: PyCharm
@Description: transfer csv to plain text. Only obtain the second field of the csv.
"""
import pandas as pd
import os

data_path = '../data/news'
news_file_name = 'news.example'
plain_file_name = 'plain_news.example'

chunk_size = 10000

csv_news_list = pd.read_csv(os.path.join(data_path, news_file_name), header=None, chunksize=chunk_size)
with open(os.path.join(data_path, plain_file_name), 'w+') as plain_read:
    for news_chunk in csv_news_list:
        content_list = []
        for id, (channel_no, content) in news_chunk.iterrows():
            content_list.append(content)

        plain_read.writelines(content_list)
