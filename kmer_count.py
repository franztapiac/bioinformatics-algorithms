"""
Franz. A Tapia Chaca
06 April 2022

Task
    Given seq, count appearances of pattern in seq (including overlaps)
"""


'''
Functions
'''


# Count appearances of kmer in text
def kmerCount(text, kmer):
    count = 0
    # text 0 to len(text) - 1
    # last k-mer of Text begins at position |Text| − k
    for i in range(len(text)-len(kmer)):                    # |text| - k checks
        if text[i:i+len(kmer)] == kmer:                     #   k checks
            count += 1
    return count


# Check if text has \n inside
def hasEOLchar(text):
    if "\n" in text:
        return True
    else:
        return False


'''
Main
'''
seq_file = open("1_2_dataset_2_6.txt", 'r')  # Contains sequence and pattern to search

# # Read all data as one string
# seq_data = seq_file.read()
# print(hasEOLchar(seq_data))

# Reset to starting reading position
seq_file.seek(0)

# Read separate lines (determined by \n)
seq_data_2 = seq_file.readlines()
# print(seq_data_2)

seq = seq_data_2[0][:-1]
# print(seq)
pattern_seq = seq_data_2[1][:-1]
# print(pattern_seq)

seq_file.close()

count_pattern_in_seq = kmerCount(seq, pattern_seq)
print(count_pattern_in_seq)

