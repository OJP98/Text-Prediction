# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Laboratorio #3 - Predicción de textos
#
# * Oscar Juárez - 17315
# * José Pablo Cifuentes - 17509
# * Paul Belches - 17088

# %%
import random
import collections
from wordcloud import WordCloud
import matplotlib
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re
import nltk
nltk.download('stopwords')

# Definirmos lista de stopwords según nltk
stopwords = stopwords.words('english')

# %% [markdown]
# ## Importación y limpieza de datos
#
# ### 1. Abrir y leer archivos.
#
# Cabe mencionar que todos los archivos fueron convertidos a minúsculas, se quitan los urls y en algunas ocasiones, la mayoría de símbolos que consideramos innecesarios. También se quitan las stopwords, los números y finalmente las apostrophes. Además, se separan oraciones mediante los símbolos de **.**, **!** y **?**. Se debe validar que no hayan espacios vacíos luego de estas oraciones.
#
# #### Caso 1: Blogs

# %%
# Se instancian arreglos
blog = []

with open('./files/en_US.blogs.txt', 'r', encoding='utf-8') as blog_txt:
    for line in blog_txt:
        # Quitar saltos de linea y pasar todo a minusculas
        line = line.rstrip('\n').lower()
        # Quitar URLS
        line = re.sub(r'^https?:\/\/.[\r\n]', '', line)
        # Quitar el resto de expresiones regulares, excepto . ? ! y '
        line = re.sub(r"[^\w.?!\d'\s]", '', line)
        # Quitar números
        line = re.sub(r'[0-9]', ' ', line)
        # Quitar espacios extra
        line = line.strip(' \t\n\r')
        # Quitamos todas las stopwords
        line = [word for word in line.split(' ') if word not in stopwords]
        line = ' '.join(line)
        # Finalmente, quitamos apostrofes
        line = line.replace("'", '')
        # Separar posibles oraciones
        dotSentences = line.split('.')
        excSentences = line.split('!')
        queSentences = line.split('?')

        # Validar y verificar que valga la pena recorrer varias oraciones
        if len(dotSentences) > 1:
            for sentence in dotSentences:
                # Por cada posible oración, debemos quitar los símbolos de puntuación
                sentence = re.sub(r'[^\w]', ' ', sentence).strip()
                if len(sentence) > 1: blog.append(sentence)

        elif len(excSentences) > 1:
            for sentence in excSentences:
                sentence = re.sub(r'[^\w]', ' ', sentence)
                if len(sentence) > 1: blog.append(sentence)

        elif len(queSentences) > 1:
            for sentence in queSentences:
                sentence = re.sub(r'[^\w]', ' ', sentence)
                if len(sentence) > 1: blog.append(sentence)

        elif len(line.split(' ')) > 1:
                line = re.sub(r'[^\w]', ' ', line).strip()
                blog.append(line)

# %% [markdown]
# #### Caso 2: Noticias
#
# Este caso tuvo un procedimiento igual al caso 1.

# %%
news = []

with open('./files/en_US.news.txt', 'r', encoding='utf-8') as news_txt:
    for line in news_txt:
        # Quitar saltos de linea y pasar todo a minusculas
        line = line.rstrip('\n').lower()
        # Quitar URLS
        line = re.sub(r'^https?:\/\/.[\r\n]', '', line)
        # Quitar el resto de expresiones regulares, excepto . ? ! y '
        line = re.sub(r"[^\w.?!\d'\s]", '', line)
        # Quitar números
        line = re.sub(r'[0-9]', ' ', line)
        # Quitar espacios extra
        line = line.strip(' \t\n\r')
        # Quitamos todas las stopwords
        line = [word for word in line.split(' ') if word not in stopwords]
        line = ' '.join(line)
        # Finalmente, quitamos apostrofes
        line = line.replace("'", '')
        # Separar posibles oraciones
        dotSentences = line.split('.')
        excSentences = line.split('!')
        queSentences = line.split('?')

        # Validar y verificar que valga la pena recorrer varias oraciones
       if len(dotSentences) > 1:
            for sentence in dotSentences:
                # Por cada posible oración, debemos quitar los símbolos de puntuación
                sentence = re.sub(r'[^\w]', ' ', sentence).strip()
                if len(sentence) > 1: news.append(sentence)

        elif len(excSentences) > 1:
            for sentence in excSentences:
                sentence = re.sub(r'[^\w]', ' ', sentence)
                if len(sentence) > 1: news.append(sentence)
        
        elif len(queSentences) > 1:
            for sentence in queSentences:
                sentence = re.sub(r'[^\w]', ' ', sentence)
                if len(sentence) > 1: news.append(sentence)

        elif len(line.split(' ')) > 1:
        line = re.sub(r'[^\w]', ' ', line).strip()
        news.append(line)

# %% [markdown]
# #### Caso 3: Twitter
# 
# En este caso, se toma cada distinto tweet como una oración. Es necesario quitar emojis y símbolos como #, $, %, !, @, etc. Además, se quitan urls y se permiten los símbolos: **.** **,** **'**

# %%
tweets = []

with open('./files/en_US.twitter.txt', 'r', encoding='utf-8') as twitter_txt:
    for line in twitter_txt:
        # Quitar \n y pasarlo a minusculas
        line = line.replace('\n', '').lower()
        # Quitar URLS
        line = re.sub(r'^https?:\/\/.[\r\n]', '', line)
        # Quitar el resto de expresiones regulares, excepto . , y '
        line = re.sub(r"[^\w.,\d'\s]", '', line)
        # Quitar números fuera de contexto
        line = re.sub('^\d+\s|\s\d+\s|\s\d+$', '', line)
        # Añadirlos a la lista de tweets
        tweets.append(line.strip())


# %%
df = pd.DataFrame(blog + news + tweets, columns=["oraciones"])
df.to_csv('oraciones.csv', index=False)


