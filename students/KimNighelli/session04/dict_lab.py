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

DICT1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chocolate'}

# Display the dictionary.

print 'The original dictionary: \n', DICT1

# Delete the entry for 'cake'.

del DICT1['cake']

# Display the dictionary.

print '\nThe dictionary missing the cake key: \n', DICT1

# Add an entry for 'fruit' with 'Mango' and display the dictionary.

DICT1['fruit'] = 'Mango'

# Display the dictionary keys.

print "\nThe keys in the dictionary are: ", DICT1.keys()

# Display the dictionary values.

print "\nThe values in the dictionary are: ", DICT1.values()

# Display whether or not 'cake' is a key in the dictionary (i.e. False) (now).

print "\nIs the key 'cake' in the dictionary anymore?"
print 'cake' in DICT1

# Display whether or not 'Mango' is a value in the dictionary.

print "\nIs the value 'Mango' in the dictionary?"
print 'Mango' in DICT1.values()

'''
Task 2

The dict() constructor builds dictionaries directly from sequences of
key-value pairs. Convert an integer number (of any size) to a
lowercase hexadecimal string prefixed with '0x'
* There is a hex function that does this! ex: hex(255)
'''
# Using the dict constructor and zip, build a dictionary of numbers from zero
# to fifteen and the hexadecimal equivalent (string is fine).

NUMBERS = range(16)
HEXES = []
for num in NUMBERS:
    HEXES.append(hex(num))

HEX_DICTIONARY = dict(zip(NUMBERS, HEXES))

print "\nThe number-hex dictionary: ", HEX_DICTIONARY

'''
Task 3
'''

# Using the dictionary from item 1: Make a dictionary using the same
# keys but with the number of 'a's in each value.

DICT_A_VALUES = {}

for key, values in DICT1.iteritems():
    DICT_A_VALUES[key] = values.count('a')

print "\nThe dictionary with the values being the number of times the letter \
    a appears in the dictionary from the first task :\n", DICT_A_VALUES


'''
Task 4
'''

# Create sets s2, s3 and s4 that contain numbers from zero through twenty,
# divisible 2, 3 and 4.
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

# If you reverse the union and intersection commands, the contents of the set
# are the same. However, when reversed (ie. FROZEN.union(PYSET)), the result
# is a frozen set. It seems like it takes on the properties of outside set

'''
Output:
The original dictionary:
{'cake': 'chocolate', 'city': 'Seattle', 'name': 'Chris'}

The dictionary missing the cake key:
{'city': 'Seattle', 'name': 'Chris'}

The keys in the dictionary are:  ['city', 'fruit', 'name']

The values in the dictionary are:  ['Seattle', 'Mango', 'Chris']

Is the key 'cake' in the dictionary anymore?
False

Is the value 'Mango' in the dictionary?
True

The number-hex dictionary:  {0: '0x0', 1: '0x1', 2: '0x2', 3: '0x3',
4: '0x4', 5: '0x5', 6: '0x6', 7: '0x7', 8: '0x8', 9: '0x9', 10: '0xa',
11: '0xb', 12: '0xc', 13: '0xd', 14: '0xe', 15: '0xf'}

The dictionary with the values being the number of times the letter a
appears in the dictionary from the first task :
{'city': 1, 'fruit': 1, 'name': 0}

Sets:
s2:  set([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
s3:  set([0, 3, 6, 9, 12, 15, 18])
s4:  set([0, 4, 8, 12, 16, 20])

Is s3 a subset of s2?
False

Is s4 a subset of s2?
True

The union of set('Pythoni') and frozenset('marathon') is :
set(['a', 'i', 'h', 'm', 'o', 'n', 'P', 'r', 't', 'y'])

The intersection of set('Pythoni') and frozenset('marathon') is :
set(['h', 't', 'o', 'n'])
'''
