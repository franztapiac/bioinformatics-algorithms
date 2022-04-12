
# generate reverse 5'-3' complement of 5'-3' DNA sequence
def reverseComplement(pattern):
    seq_len = len(pattern)
    rev_complement = ''
    for rev_nucleotide in range(-1, -seq_len - 1, -1):
        if pattern[rev_nucleotide] == 'A':
            rev_complement += 'T'
        elif pattern[rev_nucleotide] == 'C':
            rev_complement += 'G'
        elif pattern[rev_nucleotide] == 'T':
            rev_complement += 'A'
        elif pattern[rev_nucleotide] == 'G':
            rev_complement += 'C'
    return rev_complement


'''
Main
'''
seq_file = open("1_3_dataset_3_2.txt", 'r')
seq_file.seek(0)
file_data = seq_file.readlines()
seq_file.close()
sequence = file_data[0][:-1]
sequence_complement = reverseComplement(sequence)
print(sequence_complement)
