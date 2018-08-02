# coding:utf-8

import nltk

my_train_set = [
        ({'feature1':u'a'},'1'),
        ({'feature1':u'a'},'2'),
        ({'feature1':u'a'},'3'),
        ({'feature1':u'a'},'3'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ({'feature1':u'b'},'2'),
        ]
classifier = nltk.NaiveBayesClassifier.train(my_train_set)

print(classifier.classify({'feature1':u'a'}))
print(classifier.classify({'feature2':u'b'}))
