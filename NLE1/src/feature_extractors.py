'''
Created on 10 Nov 2013

@author: ps324
'''

from nltk.corpus import stopwords   # list of "useful" words 

#
def nb_feature_extractor_stopwords(amazon_review):
    # Extract all words from the review
    list_of_words = amazon_review.words()
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    # Replace all number tokens with "NUM"
    words_numbers_removed = ["NUM" if word.isdigit() else word for word in lowercase_words]
    # Filter out non-alphabetic words and stopwords.
    words = [word for word in words_numbers_removed if word.isalpha() and word not in stopwords.words('english')]
    return words

def nb_feature_extractor_lowercase(amazon_review):
    # Extract all words from the review
    list_of_words = amazon_review.words()
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    return lowercase_words

def nb_feature_extractor_num(amazon_review):
    # Extract all words from the review
    list_of_words = amazon_review.words()
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    # Replace all number tokens with "NUM"
    words_numbers_removed = ["NUM" if word.isdigit() else word for word in lowercase_words]
    return words_numbers_removed

def simple_feature_extractor_stopwords(list_of_words):
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    # Replace all number tokens with "NUM"
    words_numbers_removed = ["NUM" if word.isdigit() else word for word in lowercase_words]
    # Filter out non-alphabetic words and stopwords.
    words = [word for word in words_numbers_removed if word.isalpha() and word not in stopwords.words('english')]
    return words

def simple_feature_extractor_num(list_of_words):
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    # Replace all number tokens with "NUM"
    words_numbers_removed = ["NUM" if word.isdigit() else word for word in lowercase_words]
    return words_numbers_removed

def simple_feature_extractor_lowercase(list_of_words):
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    return lowercase_words
