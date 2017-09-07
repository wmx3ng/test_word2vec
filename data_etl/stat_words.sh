#!/usr/bin/env bash
# 统计文本中单词.
# 全部转小写；
# 标点符合替换为空格;
# 空格替换为换行符；

sed 's/./\L&/g;s/[[:punct:]]/ /g;s/[[:space:]]/\n/g' ~/Documents/dataset/englory_news/plain_news |sort |uniq -c |sort -n -k 1