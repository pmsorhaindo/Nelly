from nltk.classify.api import ClassifierI
import random

class SimpleClassifier(ClassifierI): 
 
    def __init__(self, pos, neg): 
        self._pos = pos 
        self._neg = neg 
 
    def classify(self, words): 
        score = 0 
        for pos_word in self._pos: 
            score += words.count(pos_word) 
        for neg_word in self._neg: 
            score -= words.count(neg_word) 
        if score == 0:
            score = random.random() - 0.5
        return "N" if score < 0 else "P" 
 
    def batch_classify(self, docs): 
        return [self.classify(doc) for doc in docs] 
 
    def labels(self): 
        return ("P", "N") 