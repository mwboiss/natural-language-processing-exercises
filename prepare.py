import unicodedata
import re
import json
import os
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd


def basic_clean(instr):
    '''
    Clean our data by making everything lowercase, normalize unicode characters, and removing unwanted characters
    '''
    # Lower case
    instr = instr.lower()
    # Normalize
    instr = unicodedata.normalize('NFKD' , instr).encode('ascii','ignore').decode('utf-8', 'ignore')
    # remove unwanted characters
    instr = re.sub(f"[^a-z0-9'\s]", '', instr)
    # Return the cleaned string
    return instr

def tokenize(instr):
    '''
    Tokenize the target string. We breakup words and puctuation into descrete units
    '''
    
    tokenizer = ToktokTokenizer()
    
    instr = tokenizer.tokenize(instr, return_str = True)
    
    return instr

def stem(instr):
    '''
    '''
    
    ps = nltk.porter.PorterStemmer()
    
    stems = [ps.stem(word) for word in instr.split()]
    
    instr = ' '.join(stems)
    
    return instr

def lemmatize(instr):
    '''
    
    '''
    
    wnl = nltk.stem.WordNetLemmatizer()
    
    lemmas = [wnl.lemmatize(word) for word in instr.split()]
    
    instr = ' '.join(lemmas)
    
    return instr

def remove_stopwords(instr, extra_words = [], exclude_words= []):
    '''
    
    '''
    
    stopword_list = stopwords.words('english')
    
    if exclude_words: 
        for word in exclude_words:
            stopword_list.remove(word)
    
    if extra_words:
        for word in extra_words:
            stopword_list.append(word)
    
    words = instr.split()
    
    filtered_words = [w for w in words if w not in stopword_list]
    
    words_removed = ' '.join(filtered_words)
    
    return words_removed