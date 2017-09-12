# -*- coding: utf-8 -*-

"""
@Time    : 9/12/17 11:25 AM
@Author  : wong
@E-Mail  : wmx3ng@gmail.com
@File    : word2vec.py
@Software: PyCharm
@Description: 1) read file and transfer it to code. 2) train the embedding matrix.
"""
import tensorflow as tf

from config.config import UNK_NAME
from data_etl.exact_words import separate_line

target_file = '../data/news/plain_news.example'
stat_file = '../data/news/stat'

vocabulary_size = 300000
embedding_size = 10


# read word and encode it.
def read_word_encode():
    words = []
    with open(stat_file, 'r') as stat_r:
        lines = stat_r.readlines()
        for line in lines:
            w_r = line.strip().split(' ')
            if len(w_r) == 2 and w_r[1].strip():
                words.append(w_r[1].strip())

    words = words[1 - vocabulary_size:]

    word_2_id = {}
    # add default.
    word_2_id[UNK_NAME] = len(word_2_id)
    for w in words:
        word_2_id[w] = len(word_2_id)

    id_2_word = {v: k for k, v in word_2_id.items()}

    return word_2_id, id_2_word


# read file and separate it into words.
def read_sample_file(sample_file):
    words_list = []
    with open(sample_file, 'r') as sample_read:
        lines = sample_read.readlines()
        for line in lines:
            words = separate_line(line)
            words_list.append(words)
    return words_list


# convert word list to id list.
def convert_word_2_id(words, word_2_id):
    ids = []
    for w in words:
        if w in word_2_id:
            ids.append(word_2_id[w])
        else:
            ids.append(word_2_id[UNK_NAME])

    return ids


if __name__ == '__main__':
    word_2_id, id_2_word = read_word_encode()
    words_list = read_sample_file(target_file)
    with tf.Session() as sess:
        embeddings = tf.Variable(
            tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
        sess.run(tf.global_variables_initializer())
        print(sess.run(embeddings))
        for train_inputs in words_list:
            print('--------------')
            print(train_inputs)
            embed = tf.nn.embedding_lookup(embeddings, convert_word_2_id(train_inputs, word_2_id))
            print(sess.run(embed))
            print(embed.get_shape())
