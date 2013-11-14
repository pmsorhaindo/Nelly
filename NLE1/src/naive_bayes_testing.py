'''
Created on 2 Nov 2013

@author: ps324
'''

import nle_utils
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
import feature_extractors as fe

import sys


list_of_readers = nle_utils.set_up_readers()
number_of_tests = 30

# Key parameters to control experiments
k_fold = False # ran out of time to implement this functionality this should remain as false.
k_fold_value = 10
cross_domain = "" # N.B. This value must be equal to the first value in nle_utils.list_of_amazon_categories
sample_ratio = 0.8
feature_extraction = None # The function of feature extraction to be applied
global cross_domain_testing_data # Speeding up the cross domain testing by not extracting it each time.
cross_domain_testing_data = None

# open file to write results out to
fo = open("N:\\Downloads\\NLE\\results_naive_bayes_test.txt", "wb")

if k_fold == False: # preserving functionality for when k folding isn't used
    # Main for loop of the experiment
    for x in xrange(0,number_of_tests):
    
        sys.stdout.write('TEST_NUMBER:' + str(x) + ':'),
        fo.write('TEST_NUMBER:' + str(x) + ':')
    
        # Split data into ((+ve training),(-ve training),(+ve testing, -ve testing))
        split_data = nle_utils.split_by_classification(list_of_readers,sample_ratio)
        
        #List - tuple - tuple - document #print type(split_data[0][0][0][0])
        i = 0 # iterator
        for domain_split in split_data:
            
            # if not cross domain
            if (cross_domain == ""):            
                sys.stdout.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + ":")
                fo.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + ":")
                train_nb_data, test_nb_data = nle_utils.format_for_naive_bayes(domain_split,feature_extraction)
                # train_nb_data = 1600 reviews when train ratio is 80%
                # to vary training data sizes uncomment the line below
                train_nb_data = train_nb_data
                nb_classifier = NaiveBayesClassifier.train(train_nb_data)
                sys.stdout.write("ACCURACY:" + str(accuracy(nb_classifier, test_nb_data)) + '\n')
                fo.write("ACCURACY:" + str(accuracy(nb_classifier, test_nb_data)) + '\r\n')
                #Print the features that the NB classifier found to be most important in making classifications
                #nb_classifier.show_most_informative_features()
            # if cross domain
            elif (cross_domain != ""):
                
                sys.stdout.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + " tested on " + cross_domain + ":")
                fo.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + " tested on " + cross_domain + ":")
                train_nb_data, _ = nle_utils.format_for_naive_bayes(domain_split,feature_extraction)
                
                if (cross_domain == nle_utils.list_of_amazon_categories[i]):
                    #global cross_domain_testing_data
                    _, cross_domain_testing_data = nle_utils.format_for_naive_bayes(split_data[nle_utils.list_of_amazon_categories.index(cross_domain)],feature_extraction)
                
                nb_classifier = NaiveBayesClassifier.train(train_nb_data)
                accuracy_val = accuracy(nb_classifier, cross_domain_testing_data)
                sys.stdout.write("ACCURACY:" + str(accuracy_val) + '\n')
                fo.write("ACCURACY:" + str(accuracy_val) + '\r\n')
            
            else:
                print "Incorrect cross domain value, use a vaild amazon review category or leave variable empty."
            
            i += 1
else:
    # The k - folds approach - this failed to work due to a type error in the nle_utils functions.
    for x in xrange(0,number_of_tests):
        
        # 10 folding 
        split_data = nle_utils.split_by_classification(list_of_readers,k_fold_value,k_fold)
        
        category_index = 0 # iterator
        for domain_split in split_data:
            
            # if not cross domain
            if (cross_domain == ""):
                #reduce from list of lists
                train_nb_data, test_nb_data = nle_utils.format_kfold_for_naive_bayes(domain_split, feature_extraction)
                
                print "train_nb_data"
                print train_nb_data[0]
                
                for i in range(0,k_fold_value):
                    sys.stdout.write('TEST_NUMBER:' + str(i+x*k_fold_value) + ':'),
                    fo.write('TEST_NUMBER:' + str(i+x*k_fold_value) + ':')
                    
                    sys.stdout.write("DOMAIN:" + nle_utils.list_of_amazon_categories[category_index] + ":")
                    fo.write("DOMAIN:" + nle_utils.list_of_amazon_categories[category_index] + ":")
                    
                    nb_classifier = NaiveBayesClassifier.train(train_nb_data[i])
                    sys.stdout.write("ACCURACY:" + str(accuracy(nb_classifier, test_nb_data[i])) + '\n')
                    fo.write("ACCURACY:" + str(accuracy(nb_classifier, test_nb_data[i])) + '\r\n')
               
            # if cross domain
            elif (cross_domain != ""):
                
                sys.stdout.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + " tested on " + cross_domain + ":")
                fo.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + " tested on " + cross_domain + ":")
                train_nb_data, _ = nle_utils.format_kfold_for_naive_bayes(domain_split)
                _, test_nb_data = nle_utils.format_kfold_for_naive_bayes(split_data[nle_utils.list_of_amazon_categories.index(cross_domain)])
            #TODO get accuracy for cross domain k-fold splits
            
            else:
                print "Incorrect cross domain value, use a vaild amazon review category or leave variable empty."
            
            i += 1
# Closing file and saving results
fo.close()