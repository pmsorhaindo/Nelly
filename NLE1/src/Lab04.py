from random import sample
from nltk.probability import FreqDist
from sussex_nltk.stats import evaluate_wordlist_classifier

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
    print(type(amazon_reviews[1]))
    return reduce(lambda words,review: words+review.words(), amazon_reviews, [])
 
#Create an Amazon corpus reader pointing at only book reviews
book_reader = AmazonReviewCorpusReader().category("book")
 
#In order to get even random splits, where each data set is a list of Amazon Review objects.
pos_training_data, pos_testing_data = split_data(book_reader.positive().documents()) #See the note above this code snippet for a description of the "documents" method.
neg_training_data, neg_testing_data = split_data(book_reader.negative().documents())
 
#You can also combine the training data
training_data = pos_training_data + neg_training_data
testing_data = pos_testing_data + neg_testing_data

positive_words = ["splendid","resplendent","splendiferous","good","awesome","great","cool","fantastic"]
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

#print formatted_training_data
