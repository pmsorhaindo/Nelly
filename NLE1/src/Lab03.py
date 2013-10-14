import os, collections, nltk, gzip
 
class AugSpellChecker(object):
 
    def __init__(self, probability_distribution=None):
        if probability_distribution:
            self.probabilities = probability_distribution
        else:
            #when working form home, the path below must be changed to reflect the location of the gutenberg data on your home machine
            gutenberg_spelling_training = os.path.join('t:\\','Departments','Informatics','LanguageEngineering','data','gutenberg','spelling.txt')
            with open(gutenberg_spelling_training) as fh: 
                data = fh.read()
            samples = data.split()
            fd = nltk.probability.FreqDist(samples)
            self.probabilities = nltk.probability.LidstoneProbDist(fd, 0.001)
        self.NWORDS = self.probabilities.samples()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        #Create an empty set ready to be filled with dictionary terms
        self.urban_dictionary = set()   
         
        #Get a file pointer to the compressed file containing urban dictionary terms
        f = gzip.open(os.path.join('t:\\','Departments','Informatics','LanguageEngineering','data','UrbanDictionary','terms.gz'))
         
        #Fill set with urban dictionary entries
        for line in f:
            self.urban_dictionary.add(line.strip())
         
        #Close the file
        f.close()
 
    def edits1(self,word):
        '''Generate all tokens of an edit-distance of 1 away from *word*'''
        splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes    = [a + b[1:] for a, b in splits if b]
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
        replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
        inserts    = [a + c + b for a, b in splits for c in self.alphabet]
        return set(deletes + transposes + replaces + inserts) 
 
    def known(self,words):
        '''Return only those tokens in *words* that appear in our training data.''' 
        return set(w for w in words if w in self.NWORDS)
 
    def correct(self,word):
        '''Given a word, spellcheck it'''
        if self.known([word]) or not word.isalpha(): # if *word* is known, or non-alphabetic
            return word        #then return *word*
        else:
            #Generate words 1 edit away from *word*, and store the ones that also appeared in training
            edits1away = self.edits1(word) #All words 1 edit away from *word* (including nonsense words)
            known_edits1 = self.known(edits1away) #Only those edits that are known words
            if known_edits1: #if any exist, then select the one that appeared most in training
                return max(known_edits1, key=self.probabilities.prob)
            else: #Otherwise no replacement was found, so just give up and return the original word
                
                print ("reaching for edit-distance 2")
                
                edits2away = []                
                for x in edits1away:
                    edits2awayforwordx = self.edits1(x)
                    
                    for y in edits2awayforwordx:
                        edits2away.append(y)
                    
                known_edits2 = self.known(edits2away) #Only those edits that are known words
                if known_edits2: #if any exist, then select the one that appeared most in training
                    return max(known_edits2, key=self.probabilities.prob)
                else:
                    return word


 
##Example usage:
#if "amazeballs" in urban_dictionary:
#    print "'amazeballs' is in the dictionary!"
#else:
#    print "'amazeballs' is not in the dictionary!"