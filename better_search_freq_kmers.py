"""
Franz A. Tapia Chaca
Last updated: 11 April 2022
"""

'''
Libraries & Functions
'''


def frequencyTable(text, k):
    freqMap = {}
    n = len(text)
    for i in range(n-k):
        pattern = text[i:i+k]
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] += 1
    return freqMap


# Get max count in table
def maxMap(freqTable):
    return max(freqTable.values())


# get the most frequent kmers in text
def betterFrequentWords(text, k):           # Given text and k
    frequentPatterns = []
    freqMap = frequencyTable(text, k)           # generate frequency table
    maxCount = maxMap(freqMap)                  # get max count in table

    # [k for k, v in freqTable.items() if v == maxCount] other code to get the most frequent keys
    for pattern in freqMap:
        if freqMap[pattern] == maxCount:
            frequentPatterns.append(pattern)    # store pattern if it has max count
    return frequentPatterns


'''
Main
'''
seq_file = open("1_2_dataset_2_13.txt", 'r')  # Contains sequence and pattern to search
seq_file.seek(0)
seq_data_2 = seq_file.readlines()
seq_file.close()
seq = seq_data_2[0][:-1]
k_len = int(seq_data_2[1][:-1])

mostFrequentKmers = betterFrequentWords(seq, k_len)
print(mostFrequentKmers)
