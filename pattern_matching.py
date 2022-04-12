"""
Pattern matching problem
Given a pattern and genome, find the locations of pattern in genome
"""

'''
Functions and libraries
'''
from reverse_complement import reverseComplement


# Find index locations of pattern in genome
def findLocations(substring, string, alsoComplement=False):       # assumes linear genome, not circular genome
    # A C T G A G T
    # 0 1 2 3 4 5 6
    # pattern ATC
    # iterate from 0 to 4 (length of string 7 - length of pattern 3 + 1)
    length = len(string)
    k = len(substring)
    locations = []
    complement_locations = []
    if alsoComplement:
        complement = reverseComplement(substring)
    for i in range(length-k+1):
        if substring == string[i:i+k]:
            locations.append(i)
        if alsoComplement:
            if complement == string[i:i+k]:
                complement_locations.append(i)
    return locations, complement_locations


'''
Main
'''
file = open("v_cholera_genome.txt", 'r')
file.seek(0)
file_data = file.readlines()
file.close()
pattern = 'CTTGATCAT'
genome = file_data[0][:-1]

pattern_locations, complement_pattern_locations = findLocations(pattern, genome, alsoComplement=True)
for i in range(len(pattern_locations)):
    print(pattern_locations[i], end=' ')
print('')
for i in range(len(complement_pattern_locations)):
    print(complement_pattern_locations[i], end=' ')
