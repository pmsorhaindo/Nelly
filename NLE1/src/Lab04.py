from random import sample
from random import shuffle
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from sussex_nltk.stats import evaluate_wordlist_classifier
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

import Lab05

from sussex_nltk.corpus_readers import AmazonReviewCorpusReader
 
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
    # print(type(amazon_reviews[1]))
    return reduce(lambda words,review: words+review.words(), amazon_reviews, [])

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
 

#Create an Amazon corpus reader pointing at only book reviews
book_reader = AmazonReviewCorpusReader().category("book")
 
#In order to get even random splits, where each data set is a list of Amazon Review objects.
pos_training_data, pos_testing_data = split_data(book_reader.positive().documents()) #See the note above this code snippet for a description of the "documents" method.
neg_training_data, neg_testing_data = split_data(book_reader.negative().documents())

#Get some extra book data
extra_dvd_positive = [r for r in book_reader.unlabeled(["book"]).documents() if r.rating() > 4.9 ]
extra_dvd_negative = [r for r in book_reader.unlabeled(["book"]).documents() if r.rating() < 1.1 ]
 
#You can also combine the training data
training_data = pos_training_data + neg_training_data
testing_data = pos_testing_data + neg_testing_data

data_to_shuffle = training_data
shuffled_data = shuffle(training_data)
training_data_subset = training_data[:500] # first 500 reviews

# hand crafter positive wordlist
positive_words = ["brilliant","splendid","resplendent","splendiferous","good","awesome","great","cool","fantastic",
                  "amazing","blithesome","excellent","fabulous","favorable","fortuitous","incredible","ineffable","mirthful"
                  "outstanding","perfect","propitious","remarkable","smart","spectacular","splendid","stellar","stupendous",
                  "super","ultimate","unbelievable","wondrous",]
# hand crafter negative wordlist
negative_words = ["mediocre","paltry","flakey","awful","bad","inconsequential","pathetic","fail"]






#A frequency distribution over all words in positive book reviews
pos_book_freqdist = FreqDist(get_all_words(pos_training_data))
neg_book_freqdist = FreqDist(get_all_words(neg_training_data))


#top_m_most_frequest becomes a list of the *m* most frequent words in pos_book_freqdist 
x = 30
def top_x_most_frequent(fDist_of_words,x=100):
    return fDist_of_words.keys()[:x]
#top_x_most_frequent = pos_book_freqdist.keys()[:x]

#freqs_above_count becomes a list of all words with their number of occurrences over *n* in pos_book_freqdist 
x = 250
def words_as_frequent_as_x(fDist_of_words,x=250):
    return [word for word,count in fDist_of_words.iteritems() if count > x]
#freqs_above_count = [word for word,count in list_of_words.iteritems() if count > x]

#old fails evaled at 0.4466667
#negative_book_words_list = words_as_frequent_as_x(neg_book_freqdist,250)
#positive_book_words_list = words_as_frequent_as_x(pos_book_freqdist,250)

#words
negative_book_words_list = top_x_most_frequent(neg_book_freqdist,60)
positive_book_words_list = top_x_most_frequent(pos_book_freqdist,60)

print(type(positive_book_words_list))

# classifier creation
book_classifier = Lab05.SimpleClassifier(positive_book_words_list,negative_book_words_list)
print(type(book_classifier))

intro_neg_txt = "I have a list of negative words and my classifier thinks they are "
intro_pos_txt = "I have a list of positive words and my classifier thinks they are "

print intro_neg_txt + book_classifier.classify(get_all_words(neg_testing_data))
print intro_pos_txt + book_classifier.classify(get_all_words(pos_testing_data))

#print get_all_words(neg_testing_data)
evaluate_wordlist_classifier(book_classifier,pos_testing_data,neg_testing_data)


#Format the positive and negative separately
formatted_pos_training = Lab05.format_data(pos_training_data, "pos") 
formatted_neg_training = Lab05.format_data(neg_training_data, "neg") 
formatted_training_data = formatted_pos_training + formatted_neg_training

formatted_pos_testing = Lab05.format_data(pos_testing_data, "pos") 
formatted_neg_testing = Lab05.format_data(neg_testing_data, "neg") 
formatted_testing_data = formatted_pos_testing + formatted_neg_testing


#Naive Bayes takes the marked documents in the training data and just trains on them. with .train.
# 
#Train on a list of reviews
nb_classifier = NaiveBayesClassifier.train(formatted_training_data)
 
#Test on another list of reviews
print "Accuracy:", accuracy(nb_classifier, formatted_testing_data)
 
#Print the features that the NB classifier found to be most important in making classifications
nb_classifier.show_most_informative_features() 
