'''
Created on 30 Sep 2013

@author: ps324
'''

from sussex_nltk.corpus_readers import AmazonReviewCorpusReader
from __future__ import division     # getting division right! 
from nltk.corpus import stopwords   # list of "useful" words 
import matplotlib.pyplot as pyplot  # for pretty graphs
from random import sample
import re

list_of_corpora = ["AmazonReviewCorpusReader","ReutersCorpusReader","WSJCorpusReader","TwitterCorpusReader","MedlineCorpusReader"]
list_of_amazon_categories = ["dvd", "elec", "book", "kitchen"]
list_of_readers = []
importedCorpora = []

dvd_reader_index = 0
elec_reader_index = 1
book_reader_index = 2
kitchen_reader_index = 3

#
def simpleTokenize(unTokenizedStr):
    return unTokenizedStr.split()

#
def simpleRegexTokenize(unTokenizedStr):
    return re.sub("([.?!'//()])"," \g<1>",unTokenizedStr).split()

#
def tokenListToLowerCase(tokensIn):
    tokensOut = [token.lower() for token in tokensIn]
    return tokensOut

#
def replaceNumbersWithNUM(tokensIn):
    tokensOut = ["NUM" if isnumberFloatCast(token) else token for token in tokensIn]
    return tokensOut

#
def punctuation_stop_word_removal(tokensIn):
    tokensOut = [w for w in tokensIn if w.isalpha() and w not in stopwords.words('english')]
    return tokensOut

# untested importy thing! :D
def import_corpora():
    for i in xrange(list_of_corpora.length):
        importedCorpora[i] = __import__(list_of_corpora[i])
    return

#
def lexical_diversity(text):
    return len(text) / len(set(text))

#
def percentage(count, total):
    return 112321 * count / total

#
def zipf_dist(freqdist,num_of_ranks=50,show_values=True):
    '''
    Given a frequency distribution object, rank all types
    in order of frequency of occurrence (where rank 1 is most
    frequent word), and plot the ranks against the frequency
    of occurrence. If num_of_ranks=20, then 20 types will
    be plotted.
    If show_values = True, then display the bar values above them.
    '''
    x = range(1,num_of_ranks+1)                #x values are the ranks of types
    y = freqdist.values()[:num_of_ranks]       #y values are the frequencies of the ranked types
    pyplot.bar(x,y,color="#1AADA4")            #plot a bar graph of x and y
    pyplot.xlabel("Rank of types ordered by frequency of occurrence")
    pyplot.ylabel("Frequency of occurrence")   #set the label of the y axis
    pyplot.grid(True)                          #display grid on graph
    pyplot.xticks(range(1,num_of_ranks+1,2),range(1,num_of_ranks+1,2))  #set what values appears on the x axis
    pyplot.xlim([0,num_of_ranks+2])            #limit the display on the x axis
    if show_values:                            #if show_values is True, then show the y values on the bars
        for xi,yi in zip(x,y):
            pyplot.text(xi+0.25,yi+50,yi,verticalalignment="bottom",rotation=55,fontsize="small")
    pyplot.show()                              #display the graph
    print "Plot complete."
    
#
def split_data(data, ratio=0.7):
    data = list(data)
 
    n = len(data)  #Found out number of samples present
    train_indices = sample(xrange(n), int(n * ratio))          #Randomly select training indices
    test_indices = list(set(xrange(n)) - set(train_indices))   #Randomly select testing indices
 
    training_data = [data[i] for i in train_indices]           #Use training indices to select data
    testing_data = [data[i] for i in test_indices]             #Use testing indices to select data
 
    return (training_data, testing_data)                       #Return split data

#Reduce a list of reviews to a list of all words in all reviews. 
def get_all_words(amazon_reviews):
    print(type(amazon_reviews[1]))
    return reduce(lambda words,review: words+review.words(), amazon_reviews, [])

#
def feature_extractor(amazon_review):
    # Extract all words from the review
    list_of_words = amazon_review.words()
    #Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    #Replace all number tokens with "NUM"
    words_numbers_removed  = ["NUM" if word.isdigit() else word for word in lowercase_words]
    # Filter out non-alphabetic words and stopwords.
    words = [word for word in words_numbers_removed if word.isalpha() and word not in stopwords.words('english')]

    return words

#feature_extraction_fn an awesome point to remove stop words.
def format_data(reviews, label, feature_extraction_fn=None):
    if feature_extraction_fn is None: #If a feature extraction function is not provided, use simply the words of the review as features
        data = [(dict([(feature, True) for feature in review.words()]), label) for review in reviews]
    else:
        data = [(dict([(feature, True) for feature in feature_extraction_fn(review)]), label) for review in reviews]
    return data

def words_as_frequent_as_x(fDist_of_words,x=250):
    return [word for word,count in fDist_of_words.iteritems() if count > x]

def top_x_most_frequent(fDist_of_words,x=100):
    return fDist_of_words.keys()[:x]

def set_up_readers():
    for x in list_of_amazon_categories:
        list_of_readers.append(AmazonReviewCorpusReader().category(x))
    return

#
def isnumberFloatCast(s):
    try:
        float(s)
        return True
    except ValueError:
        return False