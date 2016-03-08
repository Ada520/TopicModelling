# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 11:53:40 2014

@author: ad1154
"""

import re
import nltk



# create list of lower case words

print 'Words in text:', len(documents)
# punctuation and numbers to be removed
punctuation = re.compile(r'[-.?!,":;()/\|0-9]')
documents = [punctuation.sub("", word) for word in documents] 


texts = [unicode(d) for d in documents]