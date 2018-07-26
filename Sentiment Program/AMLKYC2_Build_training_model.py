import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize



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
    
long_CompliaceNews =open("short_reviews/Compliance_News_List.txt","r").read() 
short_ComplianceAML = open("short_reviews/Compliance_Negative_Word_List.txt","r").read()
short_pos = open("short_reviews/positive.txt","r").read()
short_neg = open("short_reviews/negative.txt","r").read()

#Initiate all_words and documents.
all_words = []
documents = []


#  J is adject, R is adverb, V is verb and N is noun.
allowed_word_types = ["J","R","V", "N"]

j = 0
#documents[j][0] shows the sentences and documents[j][1] shows the senitment judgement.
#Insert the compliance / AML list first into all_words.
for p in long_CompliaceNews.split('/////'):
    documents.append( (p, "neg") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

for p in short_ComplianceAML.split('\n'):
    documents.append( (p, "neg") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

#Insert negative news words.
for p in short_neg.split('\n'):
    documents.append( (p, "neg") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

#Insert positive news words.
for p in short_pos.split('\n'):
    documents.append( (p, "pos") )
    #print("Documents:", documents[j][0])
    #print("Sentiment:", documents[j][1])
    #j=j+1
    
    words = word_tokenize(p)

    #for w in words:
        #print("w is:", w)

    #Put taggers for the words.
    pos = nltk.pos_tag(words)

    #w[1][0] shows the taggers of the words.
    #w[0] shows the word
    #w[0][0] shows the first character of the word
    #w[0][1] shows the 2ndt character of the word
    #and so on for test part of the words.
    for w in pos:
        if w[1][0] in allowed_word_types:
            #print("Word append: ", w[0], "Tagger: ", w[1][0])
            all_words.append(w[0].lower())

#Output documents into file.
output = open("AMLKYC2_Doc/documents.txt","a")
j = 0
for p in documents:
    output.write(documents[j][0])
    output.write('\n')
    output.write(documents[j][1])
    output.write('\n')
    j=j+1
    
output.close()


save_documents = open("pickled_algos/documents.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()


all_words = nltk.FreqDist(all_words)

output = open("AMLKYC2_Doc/word_distribution.txt","a")

j = 1
output.write("Word distribution:")
output.write('\n')

for w in all_words: 
    output.write(str(j))
    output.write(" ")
    output.write(w)                  #Show the contents of w.
    output.write(" ")
    output.write(str(all_words[w]))  #Show the distribution number of w.
    output.write('\n')
    j = j + 1

output.close()

word_features = list(all_words.keys())[:5000] #Use the first 5000 all_words list.  We use .keys() to abstract the words.


#Abstract out the first [5000] features into a file named as word_features.txt
output = open("AMLKYC2_Doc/word_features.txt","a")

i = 1
for w in word_features:
    output.write(str(i))
    output.write('  ')
    output.write(w.lower())
    output.write('\n')
    i = i + 1

output.close()

save_word_features = open("pickled_algos/word_features5k.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()

#output = open("AMLKYC2_Doc/word_features_sentiment.txt","a")
def find_features(document):
    words = word_tokenize(document)    
    features = {}
    for w in word_features:
        features[w] = (w in words)
        #output.write(w)
        #output.write('  ')
        #output.write(str(features[w]))
        #output.write('\n')

    return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]

save_classifier = open("pickled_algos/featuresets.pickle","wb")
pickle.dump(featuresets, save_classifier)
save_classifier.close()

#output.close()

random.shuffle(featuresets)
print("The featuresets length is:", len(featuresets))

testing_set = featuresets[10000:]
training_set = featuresets[:10000]

#Naive Bayes Classifer
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

save_classifier = open("pickled_algos/originalnaivebayes5k.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

#MNB classifier
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

save_classifier = open("pickled_algos/MNB_classifier5k.pickle","wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

#Bernoulli NB classifier
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

save_classifier = open("pickled_algos/BernoulliNB_classifier5k.pickle","wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()

#Logistic Regression classifier
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

save_classifier = open("pickled_algos/LogisticRegression_classifier5k.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()

#Linear SVC classifier
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

save_classifier = open("pickled_algos/LinearSVC_classifier5k.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

#Nu SVC classifier
##NuSVC_classifier = SklearnClassifier(NuSVC())
##NuSVC_classifier.train(training_set)
##print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

#SGDC classifier
SGDC_classifier = SklearnClassifier(SGDClassifier())
SGDC_classifier.train(training_set)
print("SGDClassifier accuracy percent:",nltk.classify.accuracy(SGDC_classifier, testing_set)*100)

save_classifier = open("pickled_algos/SGDC_classifier5k.pickle","wb")
pickle.dump(SGDC_classifier, save_classifier)
save_classifier.close()
