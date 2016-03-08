# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 14:52:20 2014

@author: Aditya
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 11:41:12 2014

@author: Aditya
"""
import os
import glob
path = '/Users/Aditya/Documents/Project_ptucha/NSFABS/Part1/awards_1990/awd_1990_00'
filenames = os.listdir(path)
filenames = [f for f in filenames if f.find('.txt') > 0]
os.chdir(path)
documents = []
read_files = glob.glob("*.txt")
for f in read_files:
    documents.append(open(f,'r').read())
    
        
        
            
            