# Doesn't work. Kept for reference

import nltk

from nltk.corpus import movie_reviews

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words.keys())[:2000]

def document_features(document):
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

featuresets = [(document_features(d), c) for (d,c) in word_features]
classifier = nltk.NaiveBayesClassifier.train(featuresets)
classifier.classify(document_features(d))
classifier.show_most_informative_features(5)

