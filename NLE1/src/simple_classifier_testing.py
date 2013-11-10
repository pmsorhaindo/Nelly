'''
Created on 1 Nov 2013

@author: ps324
'''

import nle_utils
import simple_classifier

import sys

# Ensure Amazon readers are defined
list_of_readers = nle_utils.set_up_readers()
number_of_tests = 30

fo = open("N:\\Downloads\\NLE\\results_s.txt", "wb")

for x in xrange(0,number_of_tests):

    sys.stdout.write('TEST_NUMBER:' + str(x) + ':')
    fo.write('TEST_NUMBER:' + str(x) + ':')

    # Split data into ((+ve training),(-ve training),(+ve testing, -ve testing))
    split_data = nle_utils.split_by_classification(list_of_readers,0.8)
    
    #List - tuple - tuple - document
    #print type(split_data[0][0][0][0])
    i = 0 # iterator
    for domain_split in split_data:
        
        #print "\n for a domain " + nle_utils.list_of_amazon_categories[i] + ":"
        sys.stdout.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + ":")
        fo.write("DOMAIN:" + nle_utils.list_of_amazon_categories[i] + ":")
        # Detemine Frequency distribution of all words in training data positive and negative.
        fdists = nle_utils.calculate_training_freq_dists(domain_split)
        
        ### DECISION: top x OR more than x
        #wordlist_tuple = nle_utils.pos_neg_wordlist(fdists,nle_utils.words_as_frequent_as_x,100)
        wordlist_tuple = nle_utils.pos_neg_wordlist(fdists,nle_utils.top_x_most_frequent,100)
        #wordlist_tuple = nle_utils.positive_words, nle_utils.negative_words
        
        s = simple_classifier.SimpleClassifier(wordlist_tuple[0],wordlist_tuple[1])
        
        # domain_split[1][0] positive documents for the domains
        p = s.classify(domain_split[1][0])
        # domain_split[1][0] negative documents for the domains
        n = s.classify(domain_split[1][1])
        
        intro_pos_txt = "I have a list of positive words and my classifier thinks they are "
        intro_neg_txt = "I have a list of negative words and my classifier thinks they are "
        
        sys.stdout.write("ACCURACY:" + str(nle_utils.evaluate_wordlist_classifier(s,domain_split[1][0],domain_split[1][1])) + '\n')
        fo.write("ACCURACY:" + str(nle_utils.evaluate_wordlist_classifier(s,domain_split[1][0],domain_split[1][1])) + '\r\n')
        
        print intro_pos_txt + p
        print intro_neg_txt + n
        i += 1