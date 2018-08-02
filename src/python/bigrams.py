import nltk

def generate_model(cfdist, word, num=10):
	for i in range(num):
		print(word),
		word = cfdist[word].max()

text = nltk.corpus.genesis.words('english-kjv.txt')

bigrams = nltk.bigrams(text)

cfd = nltk.ConditionalFreqDist(bigrams)

generate_model(cfd, 'the')