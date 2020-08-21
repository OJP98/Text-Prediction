
import pandas as pd
import numpy as np
import re
import nltk
import matplotlib
from wordcloud import WordCloud
import collections
import random

blog, news, tweets = [], [], []

with open('./files/en_US.blogs.txt', 'r', encoding='utf-8') as blog_txt:
    for line in blog_txt:
        blog.append(line.lower())

with open('./files/en_US.news.txt', 'r', encoding='utf-8') as news_txt:
    for line in news_txt:
        news.append(line.lower())

with open('./files/en_US.twitter.txt', 'r', encoding='utf-8') as twitter_txt:
    for line in twitter_txt:
        # Quitar \n y pasarlo a minusculas
        line = line.replace('\n', '').lower()
        # Quitar URLS
        line = re.sub(r'^https?:\/\/.[\r\n]', '', line)
        # Quitar el resto de expresiones regulares, excepto . , y '
        line = re.sub(r"[^\w.,\d'\s]", ' ', line)
        # Quitar números fuera de contexto
        line = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", line)
        # Añadirlos a la lista de tweets
        tweets.append(line)

df = pd.DataFrame(tweets, columns=["tweets"])
df.to_csv('tweets.csv', index=False)
