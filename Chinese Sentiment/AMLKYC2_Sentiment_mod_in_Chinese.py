#File: sentiment_mod.py

import nltk
import random
import jieba
import jieba.analyse

from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode



class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

#Load the 5000 word fetures.
word_features5k_f = open("pickled_algos/word_features5k.pickle", "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()

#Load five testing models.
open_file = open("pickled_algos/originalnaivebayes5k.pickle", "rb")
NaiveBayes_classifier = pickle.load(open_file)
open_file.close()


open_file = open("pickled_algos/MNB_classifier5k.pickle", "rb")
MNB_classifier = pickle.load(open_file)
open_file.close()


open_file = open("pickled_algos/BernoulliNB_classifier5k.pickle", "rb")
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()


open_file = open("pickled_algos/LogisticRegression_classifier5k.pickle", "rb")
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()


open_file = open("pickled_algos/LinearSVC_classifier5k.pickle", "rb")
LinearSVC_classifier = pickle.load(open_file)
open_file.close()


open_file = open("pickled_algos/SGDC_classifier5k.pickle", "rb")
SGDC_classifier = pickle.load(open_file)
open_file.close()


#Voting results for the above five testing models.
#Note: we can only vote for max 5 testing models.  So, we have to comment one model out.
voted_classifier = VoteClassifier(
                                  NaiveBayes_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier,
                                  #LinearSVC_classifier,
                                  SGDC_classifier)

def find_features(document):
    words = jieba.analyse.textrank(document, topK=5000, withWeight=False)
    
    features = {}
    for w in word_features:
        #save the boolean result: True or False for the word matching.
        #if the words of features match the words in the document ==> True otherwise False.
        features[w] = (w in words)  
        #output.write(w)
        #output.write('  ')
        #output.write(str(features[w]))
        #output.write('\n')
        #print('featues are:  ' + w + '   w contents:  ' + str(features[w]) + '\n')

    return features

#Main function for the sentiment tests.
def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)

