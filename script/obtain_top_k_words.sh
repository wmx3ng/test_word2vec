#!/usr/bin/env bash

# obtain topK frequent words from data/news/stat

data_file='../data/news/stat'
target_file='../data/news/top_k'
#awk '{ if ($1 >= 10) print $2}' "$data_file" > "$target_file"
awk '{ if ( length($2) > 0 && $1 >= 10 ) print $2}'  "$data_file" > "$target_file"
