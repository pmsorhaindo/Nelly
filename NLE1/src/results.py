'''
Created on 07 Nov 2013

@author: ps324
'''


import os
import sys
import nle_utils
import numpy as np

fo = open("N:\\Downloads\\NLE\\results_nb_20131111_feature_extractor_stopwords.txt", "r")

list_of_result_lists = []
result_labels = []
test_number = 0

#
def process_line(line):
    print line
    line_elements = line.split(":")
    
    if ("TEST_NUMBER" in line_elements[0] and line_elements[1] == "0" ):
        print line_elements[1] + "before init"
        global test_number
        test_number = line_elements[1]
        result_labels.append(line_elements[3])
        val = format_accuracy_values(line_elements[5])
        list_of_result_lists.append([val])
    
    elif ("DOMAIN" in line_elements[0] and test_number == "0"):
        result_labels.append(line_elements[1])

        val = format_accuracy_values(line_elements[3])
        list_of_result_lists.append([val])
    
    elif ("TEST_NUMBER" in line_elements[0] and line_elements[1] != "0" ):
        print  line_elements[1] + "after init"
        test_number = line_elements[1]
        val = format_accuracy_values(line_elements[5])
        print "before",
        print list_of_result_lists
        list_of_result_lists[result_labels.index(line_elements[3])].append(val)
        print "after",
        print list_of_result_lists
        
    elif ("DOMAIN" in line_elements[0] and test_number != 0 ):
        #print ""
        val = format_accuracy_values(line_elements[3])
        list_of_result_lists[result_labels.index(line_elements[1])].append(val)
    else:
        print "Illegally formed results line"

def format_accuracy_values(val):
    temp_val = str(val).replace('\\n','').replace(".", "")
    temp_val = int(temp_val)
    
    #as all values are a probability between 0 and 1
    while (temp_val > 1):
        temp_val /= 10.;
    #print temp_val # accuracy retained post-file-read-in.
    return temp_val
    
        

def read_in_results():
    while 1:
        line = fo.readline()
        if not line:
            break
        process_line(line)


read_in_results()
print list_of_result_lists

averages = map(nle_utils.average_from_list ,list_of_result_lists) # list of mean values
standard_deviations = map(np.std ,list_of_result_lists)
nle_utils.plot_results(averages, "The mean values of "+ str(len(list_of_result_lists[0])) +" trial results",['elec', 'dvd', 'book', 'kitchen'],(0,1))

print averages
print standard_deviations

import matplotlib.pyplot as plt     # graph plotting


mu, sigma = 0.7847, 0.01782 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
linewidth=2, color='r')

mu, sigma = 0.7417, 0.03795 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
linewidth=2, color='b')

plt.show()

