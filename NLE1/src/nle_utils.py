'''
Created on 30 Sep 2013

@author: ps324
'''

from __future__ import division     # getting division right! 
from sussex_nltk.corpus_readers import AmazonReviewCorpusReader
from nltk.probability import FreqDist # frequency distribution objects
from nltk.corpus import stopwords   # list of "useful" words 
import matplotlib.pyplot as pyplot  # for pretty graphs
from random import sample
import re

list_of_corpora = ["AmazonReviewCorpusReader", "ReutersCorpusReader", "WSJCorpusReader", "TwitterCorpusReader", "MedlineCorpusReader"]
list_of_amazon_categories = ["dvd", "elec", "book", "kitchen"]
importedCorpora = []
#list_of_readers = []
#split_reader_data = []
#training_freq_dists

# hand crafter positive wordlist
positive_words = ["brilliant", "splendid", "resplendent", "splendiferous", "good", "awesome", "great", "cool", "fantastic",
                  "amazing", "blithesome", "excellent", "fabulous", "favorable", "fortuitous", "incredible", "ineffable", "mirthful"
                  "outstanding", "perfect", "propitious", "remarkable", "smart", "spectacular", "splendid", "stellar", "stupendous",
                  "super", "ultimate", "unbelievable", "wondrous", ]
# hand crafter negative wordlist
negative_words = ["mediocre", "paltry", "flakey", "awful", "inconsequential", "pathetic", "fail", "abandoned",
                  "abrasive", "abrupt", "abused", "aggressive", "ambiguous", "artificial", "awkward", "bad", "bizzare",
                  "blacklisted", "bleak", "boring", "bothersome", "broken", "burdensome", "chaotic", "crap", "damaged",
                  "dangerous", "dejected", "demonic", "difficult", "discarded", "faded", "gross", "hard", "thoughtless",
                  "tired", "tiresome", "undesirable", "ungainly", "unimportant", "uninformed", "unkempt", "unknown", "unruly",
                  "unsafe", "unsuitable", "unsupported", "unsure", "untoward", "unwanted", "unwieldy", "upset", "vague", "volatile",
                  "vulgar", "wasteful", "weak", "weary", "worried", "worthless", "wretched"]

dvd_reader_index = 0
elec_reader_index = 1
book_reader_index = 2
kitchen_reader_index = 3

#
def simpleTokenize(unTokenizedStr):
    return unTokenizedStr.split()

#
def simpleRegexTokenize(unTokenizedStr):
    return re.sub("([.?!'//()])", " \g<1>", unTokenizedStr).split()

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
def zipf_dist(freqdist, num_of_ranks=50, show_values=True):
    '''
    Given a frequency distribution object, rank all types
    in order of frequency of occurrence (where rank 1 is most
    frequent word), and plot the ranks against the frequency
    of occurrence. If num_of_ranks=20, then 20 types will
    be plotted.
    If show_values = True, then display the bar values above them.
    '''
    x = range(1, num_of_ranks + 1)                #x values are the ranks of types
    y = freqdist.values()[:num_of_ranks]       #y values are the frequencies of the ranked types
    pyplot.bar(x, y, color="#1AADA4")            #plot a bar graph of x and y
    pyplot.xlabel("Rank of types ordered by frequency of occurrence")
    pyplot.ylabel("Frequency of occurrence")   #set the label of the y axis
    pyplot.grid(True)                          #display grid on graph
    pyplot.xticks(range(1, num_of_ranks + 1, 2), range(1, num_of_ranks + 1, 2))  #set what values appears on the x axis
    pyplot.xlim([0, num_of_ranks + 2])            #limit the display on the x axis
    if show_values:                            #if show_values is True, then show the y values on the bars
        for xi, yi in zip(x, y):
            pyplot.text(xi + 0.25, yi + 50, yi, verticalalignment="bottom", rotation=55, fontsize="small")
    pyplot.show()                              #display the graph
    print "Plot complete."
    
# This function takes in data and ensures it has indices. Once this has been established it takes a
# percentage of these indices at random and defines these as training indices. The remaining indices
# are defined as testing indices.
def split_data(data, ratio=0.7):
    data = list(data)
 
    n = len(data)  #Found out number of samples present
    train_indices = sample(xrange(n), int(n * ratio))          #Randomly select training indices
    test_indices = list(set(xrange(n)) - set(train_indices))   #Randomly select testing indices
 
    training_data = [data[i] for i in train_indices]           #Use training indices to select data
    testing_data = [data[i] for i in test_indices]             #Use testing indices to select data
 
    return (training_data, testing_data)                       #Return split data

# Reduce a list of reviews to a list of all words in all reviews. 
def get_all_words(amazon_reviews):
    print(type(amazon_reviews[1]))
    return reduce(lambda words, review: words + review.words(), amazon_reviews, [])

#
def feature_extractor(amazon_review):
    # Extract all words from the review
    list_of_words = amazon_review.words()
    # Get lowercase versions of all the words  
    lowercase_words = [word.lower() for word in list_of_words]
    # Replace all number tokens with "NUM"
    words_numbers_removed = ["NUM" if word.isdigit() else word for word in lowercase_words]
    # Filter out non-alphabetic words and stopwords.
    words = [word for word in words_numbers_removed if word.isalpha() and word not in stopwords.words('english')]

    return words

# feature_extraction_fn an awesome point to remove stop words.
def format_data(reviews, label, feature_extraction_fn=None):
    if feature_extraction_fn is None: # If a feature extraction function is not provided, use simply the words of the review as features
        data = [(dict([(feature, True) for feature in review.words()]), label) for review in reviews]
    else:
        data = [(dict([(feature, True) for feature in feature_extraction_fn(review)]), label) for review in reviews]
    return data

def words_as_frequent_as_x(fDist_of_words, x=250):
    return [word for word, count in fDist_of_words.iteritems() if count > x]

def top_x_most_frequent(fDist_of_words, x=100):
    return fDist_of_words.keys()[:x]

def pos_neg_wordlist(training_tuple, wordlist_function ,x=250):
    pos, neg = training_tuple
    fdist_pos = wordlist_function(pos,x)
    fdist_neg = wordlist_function(neg,x)
    return (fdist_pos,fdist_neg)


def set_up_readers():
    
    list_of_readers = []
    
    for x in list_of_amazon_categories:
        if (x != "all"):
            list_of_readers.append(AmazonReviewCorpusReader().category(x))
        else:
            list_of_readers.append(AmazonReviewCorpusReader())
            
    return list_of_readers

# Splits each readers pos/neg data into training and testing data according to a user defined ratio (default 0.7).
# This function returns a tuple of tuples structure containing the split data.
def split_by_classification(list_of_readers,ratio=0.7):
    
    split_reader_data = []
    
    for reader in list_of_readers:
        pos_training_data, pos_testing_data = split_data(reader.positive().documents(), ratio) #See the note above this code snippet for a description of the "documents" method.
        neg_training_data, neg_testing_data = split_data(reader.negative().documents(), ratio)
        split_reader_data.append(((pos_training_data, neg_training_data), (pos_testing_data, neg_testing_data)))
     
    return split_reader_data

# FreqDist training data (For simple classifier)
def get_freq_distribution_of(data):
    return FreqDist(get_all_words(data))

def calculate_training_freq_dists(data):
    ((pos_training_data,neg_training_data),(_,_)) = data
    pos_training_freq = get_freq_distribution_of(pos_training_data)
    neg_training_freq = get_freq_distribution_of(neg_training_data)
    return (pos_training_freq,neg_training_freq)


def format_for_naive_bayes(pos_neg_train_test_struct):
    
    # De-construct the split data structure
    ((pos_training_data,neg_training_data),(pos_testing_data,neg_testing_data)) = pos_neg_train_test_struct
    
    #Format the positive and negative separately
    formatted_pos_training = format_data(pos_training_data, "pos") 
    formatted_neg_training = format_data(neg_training_data, "neg") 
    formatted_training_data = formatted_pos_training + formatted_neg_training
    
    formatted_pos_testing = format_data(pos_testing_data, "pos")
    formatted_neg_testing = format_data(neg_testing_data, "neg") 
    formatted_testing_data = formatted_pos_testing + formatted_neg_testing
    return (formatted_training_data,formatted_testing_data)

#
def isnumberFloatCast(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

