'''
Created on 10 Nov 2013

@author: ps324
'''

from nltk.corpus import stopwords   # list of "useful" words 

# Stop word removing feature extractor plus others. (FOR NAIVE BAYES inputs)
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

# A feature extractor removing all uppercase characters and replacing them with lowercase versions. (FOR NAIVE BAYES inputs)
def nb_feature_extractor_lowercase(amazon_review):
    # Extract all words from the review
    list_of_words = amazon_review.words()
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    return lowercase_words

# A feature extractor removing all uppercase characters and replacing them 
#with lowercase versions as well as numbers. (FOR NAIVE BAYES inputs)
def nb_feature_extractor_num(amazon_review):
    # Extract all words from the review
    list_of_words = amazon_review.words()
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    # Replace all number tokens with "NUM"
    words_numbers_removed = ["NUM" if word.isdigit() else word for word in lowercase_words]
    return words_numbers_removed

# Stop word removing feature extractor plus others. (FOR SIMPLE CLASSIFIER inputs)
def simple_feature_extractor_stopwords(list_of_words):
    # extract words using map results in list of lists here so sum is used to flatten the array.
    list_of_words = sum(map(lambda x: x.words(), list_of_words),[])
    #print list_of_words
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    # Replace all number tokens with "NUM"
    words_numbers_removed = ["NUM" if word.isdigit() else word for word in lowercase_words]
    # Filter out non-alphabetic words and stopwords.
    words = [word for word in words_numbers_removed if word.isalpha() and word not in stopwords.words('english')]
    return words

# A feature extractor removing all uppercase characters and replacing them 
#with lowercase versions as well as numbers. (FOR SIMPLE CLASSIFIER inputs) 
def simple_feature_extractor_num(list_of_words):
    # extract words using map results in list of lists here so sum is used to flatten the list.
    list_of_words = sum(map(lambda x: x.words(), list_of_words),[])
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    # Replace all number tokens with "NUM"
    words_numbers_removed = ["NUM" if word.isdigit() else word for word in lowercase_words]
    return words_numbers_removed

# A feature extractor removing all uppercase characters and replacing them with lowercase versions (FOR SIMPLE CLASSIFIER inputs)
def simple_feature_extractor_lowercase(list_of_words):
    # extract words using map results in list of lists here so sum is used to flatten the array.
    list_of_words = sum(map(lambda x: x.words(), list_of_words),[])
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    return lowercase_words
