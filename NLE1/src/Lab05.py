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



#Example usage:
 
#book_classifier = SimpleClassifier(positive_book_words_list, negative_book_words_list)


# google stop word removal
#feature_extraction_fn an awesome point to remove stop words.
def format_data(reviews, label, feature_extraction_fn=None):
    if feature_extraction_fn is None: #If a feature extraction function is not provided, use simply the words of the review as features
        data = [(dict([(feature, True) for feature in review.words()]), label) for review in reviews]
    else:
        data = [(dict([(feature, True) for feature in feature_extraction_fn(review)]), label) for review in reviews]
    return data
