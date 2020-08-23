'''
    Autores:

    Jose Cifuentes
    Paul Belches
    Oscar Juarez
'''
from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
from csv import reader
import numpy as np

NOMBRE_MODELO = 'Deep1'
NOMBRE_CSV = 'training.csv'

'''
	model=el modelo generado
	tokenizer= tokenizer generado
	max_length = el largo maximo de la secuencia
	seed_text = el texto por el cual vamos a hacer la prediccion
	n_words = la cantidad de palabras que queremos predecir

'''


def generate_seq(model, tokenizer, max_length, seed_text, n_words):
    in_text = seed_text
    # se genera n palabras
    for _ in range(n_words):
        # se pasa el texto a enteros
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        # ajustamos la secuancia al max_length
        encoded = pad_sequences([encoded], maxlen=max_length, padding='pre')
        # predice las probabiliades de cada palabra

        yhat = np.argmax(model.predict(encoded), axis=-1)
        # se pasa del index a la palabra correspondiente
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        # se agrega al input
        in_text += ' ' + out_word
    return in_text


data = ""
# Se abre el csv con la data
with open(NOMBRE_CSV, encoding="utf8") as read_obj:
    csv_reader = reader(read_obj)

    contador = 0
    # Cada linea es una oracion
    for row in csv_reader:

        if(contador == 0):
            contador += 1
            continue
        data += row[0]+"\n"


'''
	Se genera un tokenizer lo cual es 
	una representacion de enteros de 
	cada palabra en nuestra data.
'''
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
encoded = tokenizer.texts_to_sequences([data])[0]


# Obtenemos el largo de nuestro vocabulario
vocab_size = len(tokenizer.word_index) + 1

# mapeamos 2 palabras a una palabra
sequences = list()
for i in range(2, len(encoded)):
    sequence = encoded[i-2:i+1]
    sequences.append(sequence)


max_length = max([len(seq) for seq in sequences])

model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_length-1))
model.add(LSTM(50))
model.add(Dense(vocab_size, activation='softmax'))

model.load_weights(NOMBRE_MODELO)
print()
print('Escriba exit() para salir...')
print(' o ingrese una frase de mas de dos palabras :)')
while(True):
    frase = input('> ')
    if(frase == 'exit()'):
        break

    prediccion = generate_seq(
        model, tokenizer, max_length-1, ' '.join(frase.split()[-2:]), 3)

    print(' '.join(prediccion.split()[2:]))
    print()
