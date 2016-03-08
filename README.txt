LDA_v5.py is the final version of the LDA implementation used.
NMF_v2.py is the final version of the NMF implementation used.

The path to the dataset needs to be set on the the os.walk line at the top. Only the desied top level directory needs to be set. 
The program will automatically retrieve text files from any levels of subdirectories within the dataset. The path could be set to any subdirectories as a top level
directory can be set to analyze only a part of the document.

The programs read the text files, combine them into a single mega document, then carry out processing such as stopwords filtering, removal punctuation, numbers, etc.
This data is then converted into a Bag Of Words Corpus from a dictionary in the case of LDA and Term Frequency Inverse Document Frequency for the NMF.
Both the scripts filter out less frequently and too frequently occuring words with the use of stoplists. The number of topics can be set for both the algorithms within the script. The number of top words for a topic can also be set.

References:
The code used in class for the LDA topic modelling lab was referred to while implementing LDA_v5.py.