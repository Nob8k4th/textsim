import re

class Tokenizer:
    STOPWORDS = {'the','a','an','is'}
    def split_space(self, text):
        return [x for x in text.split() if x]
    def split_punct(self, text):
        return [x for x in re.split(r'[^A-Za-z0-9]+', text) if x]
    def remove_stopwords(self, tokens):
        return [x for x in tokens if x not in self.STOPWORDS]
