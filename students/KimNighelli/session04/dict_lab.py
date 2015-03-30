'''
The following assignment is for the Dictionary Lab - Task 9 Assignment
It is a series of tasks that are five tasks. I will mark each section with
a series of single quotes  and each 'task' with a pound sign '#'.

Kimberlee Nighelli - March 26, 2015

'''

'''
Section 1
'''

# Create a dictionary containing 'name', 'city', and 'cake' for
# 'Chris' from 'Seattle' who likes 'Chocolate'.

DICT1 = {'name' : 'Chris', 'city' : 'Seattle', 'cake' : 'chocolate'}

#Display the dictionary.

print 'The original dictionary: \n', DICT1

#Delete the entry for 'cake'.

del DICT1['cake']

#Display the dictionary.

print '\nThe dictionary missing the cake key: \n', DICT1

#Add an entry for 'fruit' with 'Mango' and display the dictionary.

DICT1['fruit'] = 'Mango'

# Display the dictionary keys.

print "\nThe keys in the dictionary are: ", DICT1.keys()

# Display the dictionary values.

print "\nThe values in the dictionary are: ", DICT1.values()

#Display whether or not 'cake' is a key in the dictionary (i.e. False) (now).

print "\nIs the key 'cake' in the dictionary anymore?"
print 'cake' in DICT1

#Display whether or not 'Mango' is a value in the dictionary.

print "\nIs the value 'Mango' in the dictionary?"
print 'Mango' in DICT1.values()

'''
Task 2

The dict() constructor builds dictionaries directly from sequences of key-value pairs
Convert an integer number (of any size) to a lowercase hexadecimal string prefixed with '0x'
* There is a hex function that does this! ex: hex(255)
'''
# Using the dict constructor and zip, build a dictionary of numbers from zero to
# fifteen and the hexadecimal equivalent (string is fine).

NUMBERS = range(16)
HEXES = []
for num in NUMBERS:
    HEXES.append(hex(num))

HEX_DICTIONARY = dict(zip(NUMBERS, HEXES))

print "\nThe number-hex dictionary: ", HEX_DICTIONARY

'''
Task 3
'''

#Using the dictionary from item 1: Make a dictionary using the same
# keys but with the number of 'a's in each value.

DICT_A_VALUES = {}

for key, values in DICT1.iteritems():
    DICT_A_VALUES[key] = values.count('a')

print "\nThe dictionary with the values being the number of times the letter a appears \
in the dictionary from the first task :\n", DICT_A_VALUES


'''
Task 4
'''

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
S2 = set(range(0, 21, 2))
S3 = set(range(0, 21, 3))
S4 = set(range(0, 21, 4))

# Display the sets.
print "\nSets:"
print "s2: ", S2
print "s3: ", S3
print "s4: ", S4

# Display if s3 is a subset of s2 (False) and if s4 is a subset of s2 (True).

print "\nIs s3 a subset of s2?"
print S3.issubset(S2)

print "\nIs s4 a subset of s2?"
print S4.issubset(S2)

'''
Task 5
'''

# Create a set with the letters in 'Python' and add 'i' to the set.
PYSET = set('Python')
PYSET.add('i')

# Create a FROZENset with the letters in 'marathon'
FROZEN = frozenset('marathon')

# Display the union and intersection of the two sets.
print "\nThe union of set('Pythoni') and frozenset('marathon') is : "
print PYSET.union(FROZEN)

print "\nThe intersection of set('Pythoni') and frozenset('marathon') is : "
print PYSET.intersection(FROZEN)

# If you reverse the union and intersection commands, the contents of the set are
# the same. However, when reversed (ie. FROZEN.union(PYSET)), the result is a
# frozen set. It seems like it takes on the properties of outside set

