# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Laboratorio #3 - Predicción de textos
#
# * Oscar Juárez - 17315
# * José Pablo Cifuentes - 17509
# * Paul Belches - 17088

# %%
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Dense
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer
from numpy import array
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

# Para el modelo

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
                if len(sentence) > 1:
                    blog.append(sentence)

        elif len(excSentences) > 1:
            for sentence in excSentences:
                sentence = re.sub(r'[^\w]', ' ', sentence)
                if len(sentence) > 1:
                    blog.append(sentence)

        elif len(queSentences) > 1:
            for sentence in queSentences:
                sentence = re.sub(r'[^\w]', ' ', sentence)
                if len(sentence) > 1:
                    blog.append(sentence)

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
                if len(sentence) > 1:
                    news.append(sentence)

        elif len(excSentences) > 1:
            for sentence in excSentences:
                sentence = re.sub(r'[^\w]', ' ', sentence)
                if len(sentence) > 1:
                    news.append(sentence)

        elif len(queSentences) > 1:
            for sentence in queSentences:
                sentence = re.sub(r'[^\w]', ' ', sentence)
                if len(sentence) > 1:
                    news.append(sentence)

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
complete_data = blog + news + tweets
random.shuffle(complete_data)


# %%
data_size = int(len(complete_data)*0.005)
print('Se va a utilizar ' + str(data_size) + ' datos')
data = complete_data[:data_size]

# %% [markdown]
# Crear CSV con las palabras utilizadas para el entrenamiento

# %%
df = pd.DataFrame(data, columns=["oraciones"])
df.to_csv('training.csv', index=False)

# %% [markdown]
# Se genera un tokenizer lo cual es una representacion de enteros de cada palabra en nuestra data.

# %%
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
encoded = tokenizer.texts_to_sequences([data])[0]


# %%
# Obtenemos el largo de nuestro vocabulario
vocab_size = len(tokenizer.word_index) + 1


# %%
# mapeamos 2 palabras a una palabra
sequences = list()
for i in range(2, len(encoded)):
    sequence = encoded[i-2:i+1]
    sequences.append(sequence)

max_length = max([len(seq) for seq in sequences])
sequences = pad_sequences(sequences, maxlen=max_length, padding='pre')

# %% [markdown]
# separamos en los elementos inputs y outputs
#

# %%
sequences = array(sequences)
X, y = sequences[:, :-1], sequences[:, -1]
y = to_categorical(y, num_classes=vocab_size)

# %% [markdown]
# Definimos el modelo

# %%
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_length-1))
model.add(LSTM(50))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())

# %% [markdown]
# Compilamos el modelo

# %%
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])


# %%
# Entrenaoms el modelo
model.fit(X, y, epochs=150, verbose=2)


# %%
model.save_weights('deep_no_stopwords')
