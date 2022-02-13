#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 23:04:31 2022

@author: lukeum
"""

import re
import argparse
import pandas as pd


def extract_wordlist(args):
    
    cutoff = args.cutoff
    words = []
    with open(args.path,'r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if int(line[-1])>= cutoff:
                if not re.search(r'[\d\W]',line[1]):
                    words.append(line[1])
                    
    with open(args.outpath,'w') as out:
        for word in words:
            out.write(word+'\n')


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    parser.add_argument('--outpath', type=str)
    parser.add_argument('--cutoff', type=int, default=10,
                        help='an integer for the accumulator')    
    args = parser.parse_args()
    
    extract_wordlist(args)
    
