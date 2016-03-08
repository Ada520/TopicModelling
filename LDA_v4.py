# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 21:11:49 2014

@author: ad1154
"""




from gensim import corpora, models, similarities
from gensim.corpora import Dictionary, MmCorpus
from itertools import chain

from nltk.corpus import stopwords
import re
import fnmatch
import os

matches = []
documents = []
for root, dirnames, filenames in os.walk('C:\\Users\\ad1154\\Documents\\project_mil\\NSFData\\Part1\\'):
  for filename in fnmatch.filter(filenames, '*.txt'):
      matches.append(os.path.join(root, filename))

for m in matches:
    documents.append(open(m,'r').read())
    


punctuation = re.compile(r'[-.?!,":;()/\|0-9]')   # Strip all Punctuation
documents = [punctuation.sub("", do) for do in documents] 
documents = [unicode(d) for d in documents]    # Convert to Unicode      

#os.chdir('C:\\Users\\ad1154\\Documents\\project_mil\\NSFData\\')       
        
#with open("NSFMegaDump.txt", "wb") as outfile:
#    for d in documents:
#        outfile.write(d)       
#        
        
stoplist = stopwords.words('english')
texts = [[word for word in document.lower().split() if word not in stoplist]
 for document in documents]


from gensim.models import LdaModel
Num_Topics  = 10
DICT       = 'dict.bow.dict'
BOW        = 'bow.mm'
NSFLDA        = 'NSF.%03d.lda' % Num_Topics


print 'Building dictionary of terms ...'
dictionary = corpora.Dictionary(texts)
print '%d word types' % len(dictionary)

print 'Filtering infrequent and frequent terms ...'
dictionary.filter_extremes(no_below=5, no_above=0.5)
print '%d word types, after filtering' % len(dictionary)

print 'Saving dictionary (%s)...' % DICT
dictionary.save(DICT)

print 'Building bag-of-words corpus ...'
bow_corpus = [ dictionary.doc2bow(t) for t in texts ]

print 'Serializing corpus (%s) ...' % BOW
MmCorpus.serialize(BOW, bow_corpus)

size = len(bow_corpus) * 4 / 5
training = bow_corpus[:size]
testing = bow_corpus[size:]

print 'Training LDA w/ %d topics on first %d texts ...' % (Num_Topics, len(training))
lda = LdaModel(training, id2word=dictionary, num_topics=Num_Topics, passes=5, iterations = 1000)

print 'Saving LDA model (%s) ...' % NSFLDA
lda.save(NSFLDA)

print 'Random subset of topics:'
print '\n'.join(lda.print_topics())

print 'Computing perplexity on %d held-out documents ...' % len(testing)
perplexity = 2 ** -(lda.log_perplexity(testing))
print 'Perplexity: %.2f' % perplexity




