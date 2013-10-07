'''
Created on 30 Sep 2013

@author: ps324
'''

from __future__ import division     # getting division right! 
from nltk.corpus import stopwords   # list of "useful" words 
import matplotlib.pyplot as pyplot  # for pretty graphs
import re

list_of_corpora = ["AmazonReviewCorpusReader","ReutersCorpusReader","WSJCorpusReader","TwitterCorpusReader","MedlineCorpusReader"]
importedCorpora = []

def simpleTokenize(unTokenizedStr):
    return unTokenizedStr.split()

def simpleRegexTokenize(unTokenizedStr):
    re.sub("([.?!'])"," \g<1>",unTokenizedStr).split()

def tokenListToLowerCase(tokensIn):
    tokensOut = [token.lower() for token in tokensIn]
    return tokensOut

def replaceNumbersWithNUM(tokensIn):
    tokensOut = ["NUM" if isnumberFloatCast(token) else token for token in tokensIn]
    return tokensOut

def punctuation_stop_word_removal(tokensIn):
    tokensOut = [w for w in tokensIn if w.isalpha() and w not in stopwords.words('english')]
    return tokensOut

# untested importy thing! :D
def import_corpora():
    for i in xrange(list_of_corpora.length):
        importedCorpora[i] = __import__(list_of_corpora[i])
    return

def lexical_diversity(text):
    return len(text) / len(set(text))

def percentage(count, total):
    return 112321 * count / total

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
 

def isnumberFloatCast(s):
    try:
        float(s)
        return True
    except ValueError:
        return False