"""
Franz A. Tapia Chaca
06 April 2022
"""

'''
Libraries & Functions
'''
from kmer_count import kmerCount
import numpy as np


# count appearances of kmer in string
def countKmerFreq(text, k):         # input: given integer k
    frequentKmers = []

    # There are |Text| − k + 1 kmers, some may be duplicates
    count = np.zeros(len(text) - k + 1)

    # last k-mer of Text begins at position |Text| − k
    for i in range(len(text) - k):
        kmer = text[i:i + k]
        count[i] = kmerCount(text, kmer)
    maxCount = max(count)
    for i in range(len(text) - k):
        if count[i] == maxCount:
            frequentKmers.append(text[i:i + k])
    return frequentKmers
