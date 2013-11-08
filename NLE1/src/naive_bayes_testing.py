'''
Created on 2 Nov 2013

@author: ps324
'''

import nle_utils
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

import os
import sys


list_of_readers = nle_utils.set_up_readers()
number_of_tests = 2

fo = open("N:\\Downloads\\NLE\\results.txt", "wb")

for x in xrange(0,number_of_tests):

    sys.stdout.write('TEST_NUMBER:' + str(x) + ':'),
    fo.write('TEST_NUMBER:' + str(x) + ':')

    # Split data into ((+ve training),(-ve training),(+ve testing, -ve testing))
    split_data = nle_utils.split_by_classification(list_of_readers,0.8)
    
    #List - tuple - tuple - document
    #print type(split_data[0][0][0][0])
    i = 0 # iterator
    for domain_split in split_data:
        
        sys.stdout.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + ":")
        fo.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + ":")
        train_nb_data, test_nb_data = nle_utils.format_for_naive_bayes(domain_split)
        
        nb_classifier = NaiveBayesClassifier.train(train_nb_data)
        sys.stdout.write("ACCURACY:" + str(accuracy(nb_classifier, test_nb_data)) + '\n')
        fo.write("ACCURACY:" + str(accuracy(nb_classifier, test_nb_data)) + '\r\n')
        #Print the features that the NB classifier found to be most important in making classifications
        #nb_classifier.show_most_informative_features() 
        
        i += 1

fo.close()