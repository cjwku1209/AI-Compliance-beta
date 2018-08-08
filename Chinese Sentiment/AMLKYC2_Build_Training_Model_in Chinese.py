# encoding=utf-8
#For detailed definition, please refer https://github.com/fxsjy/jieba.

import nltk
import jieba
import pickle
import random
import jieba.analyse
import jieba.posseg as pseg
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify.scikitlearn import SklearnClassifier

Pos_News = open("Database/positive.txt","r", encoding="utf-8").read()
Neg_News = open("Database/negative.txt","r", encoding="utf-8").read()

#Initiate all_words and documents.
all_words = []
documents = []


j = 0
#documents[j][0] shows the sentences and documents[j][1] shows the senitment judgement.
#Insert the compliance / AML list first into all_words.
for p in Neg_News.split('/////'):
    documents.append( (p, "neg") )

for p in Pos_News.split('/////'):
    documents.append( (p, "pos") )


#Output documents into file.
output = open("Doc_Output/documents.txt","a", encoding="utf-8")
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



#Use text rank method to abstract the key words. We can use topK
#to define the top key words to be shown.

seg_list_Text_Rank = []

i = 0
j = 0
print('Show text rank scores.')
for p in documents:
  sentence = documents[j][0]
  for x, w in jieba.analyse.textrank(sentence, topK=5000, withWeight=True):
    #print(str(i+1) + ' ' + '%s %s' % (x, w))   #Show the weight factor scores.
    seg_list_Text_Rank.append(x)
    i = i + 1

  j = j + 1
   
print('\n')


output = open("Doc_Output/seg_list_Text_Rank.txt","a", encoding="utf-8")

i = 0
output.write("Segment list:")
output.write('\n')

for w in seg_list_Text_Rank:
   output.write(str(i+1))
   output.write(' ')
   output.write(w)
   output.write('\n')
   i = i + 1
   
output.close()


#Count the frequency of the key words."
all_words = nltk.FreqDist(seg_list_Text_Rank)

output = open("Doc_Output/word_distribution.txt","a", encoding="utf-8")

j = 0
output.write("Word distribution:")
output.write('\n')

for w in all_words:
    output.write(str(j+1))
    output.write(" ")
    output.write(w)                  #Show the contents of w.
    output.write(" ")
    output.write(str(all_words[w]))  #Show the distribution number of w.
    output.write('\n')
    j = j + 1

output.close()

#Train the model.
#Abstract out the first [5000] features into a file named as word_features.txt
word_features = list(all_words.keys())[:5000]
output = open("Doc_Output/word_features.txt","a", encoding="utf-8")

i = 1
for w in word_features:
    output.write(str(i))
    output.write('  ')
    output.write(w)
    output.write('\n')
    i = i + 1

output.close()


save_word_features = open("pickled_algos/word_features5k.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()


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



#Form the feature sets for training model.
#Abstract the documents into text and category, i.e. positive or negative.
#Then, find the feature matching results for the text comparing with the 5000 word_features.

#output = open("Doc_Output/word_features_sentiment.txt","a", encoding="utf-8") 

featuresets = [(find_features(rev), category) for (rev, category) in documents]

save_classifier = open("pickled_algos/featuresets.pickle","wb")
pickle.dump(featuresets, save_classifier)
save_classifier.close()

#output.close()

random.shuffle(featuresets)
feature_length = len(featuresets)
print("The featuresets length is:", feature_length)

#Left 5 datasets as testing set and make the left as training set.
training_data_numb = feature_length-5
testing_set = featuresets[training_data_numb:]
training_set = featuresets[:training_data_numb]

#Test the training models by using different methods. 
#Naive Bayes Classifer
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
#classifier.show_most_informative_features(15)

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

#SGDC classifier
#Because of new features added, we will receive alert messages for the default settings.
SGDC_classifier = SklearnClassifier(SGDClassifier())
SGDC_classifier.train(training_set)
print("SGDClassifier accuracy percent:",nltk.classify.accuracy(SGDC_classifier, testing_set)*100)

save_classifier = open("pickled_algos/SGDC_classifier5k.pickle","wb")
pickle.dump(SGDC_classifier, save_classifier)
save_classifier.close()

