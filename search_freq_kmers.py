"""
Franz A. Tapia Chaca
Last updated: 11 April 2022
"""

'''
Libraries & Functions
'''
from kmer_count import kmerCount
import numpy as np


# count appearances of kmer in string
def countKmerFrequency(text, k):         # input: given integer k
    frequentKmers = []

    # There are |Text| − k + 1 kmers, some may be duplicates
    # 0 1 2 3 4         python index
    # A C T G A         |Text| = 5, k = 3
    # 1 1 1             |Text| - 3 + 1 = 3
    currentCount = np.zeros(len(text) - k + 1)

    # last k-mer of Text begins at position |Text| − k (see above)
    # 1. count frequency of each kmer
    for i in range(len(text) - k):                  # |text| - k iterations
        kmer = text[i:i + k]
        currentCount[i] = kmerCount(text, kmer)         # ( |text| - k ) k
    maxCount = max(currentCount)

    # 2. identify most frequent kmer and store if not already saved
    for i in range(len(text) - k):                  # |text| - k
        if currentCount[i] == maxCount:
            if text[i:i + k] not in frequentKmers:
                frequentKmers.append(text[i:i + k])
    return frequentKmers
