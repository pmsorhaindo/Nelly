'''
Created on 7 Oct 2013

@author: ps324
'''

import re           #import regex module
import nle_utils    #import utils

from nltk.tokenize import word_tokenize

from sussex_nltk.corpus_readers import ReutersCorpusReader                #import the corpus reader
from sussex_nltk.corpus_readers import TwitterCorpusReader                #import the corpus reader
from sussex_nltk.corpus_readers import MedlineCorpusReader                #import the reader
from sussex_nltk.tokenize import twitter_tokenize,twitter_tokenize_batch  #import CMU tokenize functions

tcr = TwitterCorpusReader()         #create a new Twitter corpus reader
mcr = MedlineCorpusReader()         #create a new corpus reader
rcr = ReutersCorpusReader()    #Create a new reader
#for sentence in mcr.sample_raw_sents(10):          #get 100 random sentences, where each sentence is a string
    #print nle_utils.simpleRegexTokenize(sentence)   #print sentence
    #print sentence
    
#Split the example string by whitespace alone
#print "   What    is the    air-speed   velocity of  an unladen swallow?   ".split()
#print nle_utils.simpleRegexTokenize("   What    is the    air-speed   velocity of  an unladen swallow?   ")

#print re.sub("([.?!'])"," \g<1>","You're using coconuts!").split()
#print nle_utils.simpleRegexTokenize("You're using coconuts!")


sentences = []


for sentence in tcr.sample_raw_sents(10):
    sentences.append(sentence)
    
for token in twitter_tokenize_batch(sentences):   #batch tokenize a list of sentences
    print token