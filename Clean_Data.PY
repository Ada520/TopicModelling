# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 20:48:59 2014

@author: ad1154
"""
import fnmatch
import os

matches = []
documents = []
for root, dirnames, filenames in os.walk('C:\\Users\\ad1154\\Documents\\project_mil\\NSFData\\'):
  for filename in fnmatch.filter(filenames, '*.txt'):
      matches.append(os.path.join(root, filename))

for m in matches:
    documents.append(open(m,'r').read())
    
os.chdir('C:\\Users\\ad1154\\Documents\\project_mil\\NSFData\\')       
        
with open("NSFMegaDump.txt", "wb") as outfile:
    for d in documents:
        outfile.write(d)       
        
        
        
        
        
        
        
#with open("result.txt", "wb") as outfile:
#    for f in read_files:
#        with open(f, "rb") as infile:
#            outfile.write(infile.read())      