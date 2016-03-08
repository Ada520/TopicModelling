# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 21:11:49 2014

@author: ad1154
"""

from __future__ import print_function
from time import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import re
import fnmatch
import os

matches = []
documents = []
for root, dirnames, filenames in os.walk('C:\\Users\\ad1154\\Documents\\project_mil\\NSFData\\Part3\\awards_2003'):
  for filename in fnmatch.filter(filenames, '*.txt'):
      matches.append(os.path.join(root, filename))

for m in matches:
    documents.append(open(m,'r').read())
    


punctuation = re.compile(r'[-.?!,":;()/\|0-9]')   # Strip all Punctuation
documents = [punctuation.sub("", do) for do in documents] 

documents = [unicode(d) for d in documents]    # Convert to Unicode    

#size = len(documents) * 4 / 5
#training = documents[:size]
#testing = documents[size:]


n_samples = 2000
n_features = 1000
n_topics = 10
n_top_words = 10



## Feature Extraction
print("Loading dataset and extracting TF-IDF features...")


vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=n_features,
                             stop_words='english')
#training = vectorizer.fit_transform(training)
#testing = vectorizer.fit_transform(testing)
documents = vectorizer.fit_transform(documents)
t0 = time()
## Training NMF
nmf = NMF(n_components=n_topics, random_state=1).fit(documents)
print("done in %0.3fs." % (time() - t0))
feature_names = vectorizer.get_feature_names()

for topic_idx, topic in enumerate(nmf.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                    for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()
    
print(nmf.reconstruction_err_)
print(nmf.components_)