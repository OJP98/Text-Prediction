import pandas as pd
import numpy as np
import re
import nltk
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import collections
import random

blog, news, tweets = [], [], []

cont = 0
with open('./en_US.blogs.txt', 'r', encoding='utf-8') as blog_txt:
    for line in blog_txt:
        # Quitar \n y pasarlo a minusculas
        line = line.replace('\n', '').lower()
        # Quitar URLS
        line = re.sub(r'^https?:\/\/.[\r\n]', '', line)
        # Quitar el resto de expresiones regulares, excepto . , y '
        line = re.sub(r"[^\w.,\d'\s]", ' ', line)
        # Quitar números fuera de contexto
        line = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", line)
        # Añadirlos a la lista de tweets
        blog.append(line)
        cont+=1
        if (cont == 50000):
            break

cont = 0
with open('./en_US.news.txt', 'r', encoding='utf-8') as news_txt:
    for line in news_txt:
        news.append(line.lower())
        # Quitar \n y pasarlo a minusculas
        line = line.replace('\n', '').lower()
        # Quitar URLS
        line = re.sub(r'^https?:\/\/.[\r\n]', '', line)
        # Quitar el resto de expresiones regulares, excepto . , y '
        line = re.sub(r"[^\w.,\d'\s]", ' ', line)
        # Quitar números fuera de contexto
        line = re.sub("^\d+\s|\s\d+\s|\s\d+$", " ", line)
        # Añadirlos a la lista de tweets
        news.append(line)
        cont+=1
        if (cont == 50000):
            break

cont = 0
with open('./en_US.twitter.txt', 'r', encoding='utf-8') as twitter_txt:
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
        cont+=1
        if (cont == 50000):
            break

comment_words = ''
comment_words_tweet = ''
comment_words_news = ''
comment_words_blog = ''
stopwords = set(STOPWORDS) 
for sentence in tweets:
    # split the value   
    tokens = sentence.split() 
    comment_words += " ".join(tokens)+" "
    comment_words_tweet += " ".join(tokens)+" "

for sentence in news:
    # split the value   
    tokens = sentence.split() 
    comment_words += " ".join(tokens)+" "
    comment_words_news += " ".join(tokens)+" "

for sentence in blog:
    # split the value   
    tokens = sentence.split() 
    comment_words += " ".join(tokens)+" "
    comment_words_blog += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words_tweet) 

# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words_blog) 

# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words_news) 

# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 

wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(comment_words) 

# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show() 