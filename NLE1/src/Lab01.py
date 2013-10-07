import nle_utils

from nltk.text import Text
from nltk.book import *

from sussex_nltk.corpus_readers import AmazonReviewCorpusReader     #import reader class
from sussex_nltk.corpus_readers import ReutersCorpusReader          #import reader
from sussex_nltk.corpus_readers import WSJCorpusReader              #import the corpus reader
from sussex_nltk.corpus_readers import TwitterCorpusReader          #import the corpus reader
from sussex_nltk.corpus_readers import MedlineCorpusReader          #import the reader

candidateNum = 119875

arcr = AmazonReviewCorpusReader()         #create new reader
 
#positive_reviews = arcr.positive()         #store a reader pointing at all positive reviews
#negative_reviews = arcr.negative()         #pointing at all negative
#dvd_reviews = arcr.category("dvd")          #pointing at all dvd
#positive_dvd_reviews = dvd_reviews.positive()     #pointing at all postive dvd
 
#get a sample of the tokens in positive dvd reviews using your 5-digit candidate number
#tokens = positive_dvd_reviews.sample_words(candidateNum)
#for token in tokens:                             #iterate over the tokens
#    print token                                  #print each token
    

 
rcr = ReutersCorpusReader()            #Create new reader
#sport_cr = rcr.category("sport")       #Create a reader pointing at sport articles only
#finance_cr = rcr.category("finance")   #Create a reader pointing at finance articles only
# 
#Get a sample of the tokens in sport articles using your 5-digit candidate number
#tokens = sport_cr.sample_words(candidateNum)  
#for token in tokens:                   #iterate over the tokens
#    print token                        #Print each token

 
wsjcr = WSJCorpusReader()             #create a new WSJ corpus reader
 
#get a sample of tokens in the corpus using your 5-digit candidate number
#tokens = wsjcr.sample_words(candidateNum) 
#for token in tokens:                  #iterate over the tokens       
#    print token                       #print each token

 
tcr = TwitterCorpusReader()         #create a new Twitter corpus reader
 
#get a sample of tokens in the corpus using your 5-digit candidate number
#tokens = tcr.sample_words(candidateNum) 
#for token in tokens:                #iterate over the tokens
#    print token                     #print each token
 
mcr = MedlineCorpusReader()         #create a new corpus reader
 
#get a sample of tokens in the corpus using your 5-digit candidate number
tokens = mcr.sample_words(candidateNum)    

tokens = nle_utils.tokenListToLowerCase(tokens)
tokens = nle_utils.replaceNumbersWithNUM(tokens)
tokens = nle_utils.punctuation_stop_word_removal(tokens)

#for token in tokens:    #iterate over the tokens
#    print token         #print each token
    
text = Text(tokens)     #create a new Text object, providing a list of tokens from a corpus

nle_utils.zipf_dist(FreqDist(text1),40)