# code courtesy of https://nlpforhackers.io/language-models/

from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict

# Create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))

'''
contador=0
for sentence in reuters.sents():
	print(sentence)
	print()
	contador+=1

	if(contador==2):
		break

'''

#Modelo

# Count frequency of co-occurance  
for sentence in reuters.sents():
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        model[(w1, w2)][w3] += 1
 
# Let's transform the counts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count


#Prediccion
#print(dict(model["today","the"]))

d=dict(model["today","the"])

a = sorted(d.items(), key=lambda x: x[1])


print(a[-1][0])
print(a[-2][0])
print(a[-3][0])