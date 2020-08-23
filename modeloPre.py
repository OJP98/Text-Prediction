# Basado en https://nlpforhackers.io/language-models/

'''
	Autores:

	Jose Cifuentes
	Paul Belches
	Oscar Juarez
'''

from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
from csv import reader


oraciones=[]

# open file in read mode
with open('training.csv', encoding="utf8") as read_obj:
	# pass the file object to reader() to get the reader object
	csv_reader = reader(read_obj)

	contador=0

	# Iterate over each row in the csv using reader object
	for row in csv_reader:

		if(contador==0):
			contador+=1
			continue
		# row variable is a list that represents a row in csv
		oraciones.append(row[0].split())



# Create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))



#Modelo

# Count frequency of co-occurance  
for sentence in oraciones:
	for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
		model[(w1, w2)][w3] += 1
 
# Let's transform the counts to probabilities
for w1_w2 in model:
	total_count = float(sum(model[w1_w2].values()))
	for w3 in model[w1_w2]:
		model[w1_w2][w3] /= total_count


def predecir(entrada):
	try:
		entradaList=entrada.split()
		concatenar=''

		for _ in range(3):
			d=dict(model[entradaList[-2],entradaList[-1]])
			a = sorted(d.items(), key=lambda x: x[1])

			entradaList.append(a[-1][0])

			concatenar+=a[-1][0]+" "

		return concatenar
	except:
		return "Error."





print('Escriba exit() para salir...')
print(' o ingrese una frase de mas de dos palabras :)')
while(True):
	frase = input('> ')
	if(frase == 'exit()'):
		break
	print(predecir(frase))    
	print()