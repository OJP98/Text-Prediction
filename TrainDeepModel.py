from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
from csv import reader

NOMBRE_CSV='oraciones.csv'
NOMBRE_MODELO='testDeep'





data=""
# Se abre el csv con la data
with open(NOMBRE_CSV, encoding="utf8") as read_obj:
	csv_reader = reader(read_obj)

	contador=0
	#Cada linea es una oracion 
	for row in csv_reader:

		if(contador==0):
			contador+=1
			continue
		data+=row[0]+"\n"


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
sequences = pad_sequences(sequences, maxlen=max_length, padding='pre')

# separamos en los elementos inputs y outputs
sequences = array(sequences)
X, y = sequences[:,:-1],sequences[:,-1]
y = to_categorical(y, num_classes=vocab_size)

# Definimos el modelo
model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=max_length-1))
model.add(LSTM(50))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())

# Compilamos el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenaoms el modelo
model.fit(X, y, epochs=500, verbose=2)

model.save_weights(NOMBRE_MODELO)

