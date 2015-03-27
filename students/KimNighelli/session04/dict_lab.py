'''
The following assignment is for the Dictionary Lab - Task 9 Assignment. 
It is a series of tasks that are five tasks. I will mark each section with 
a series of single quotes  and each 'task' with a pound sign '#'.

Kimberlee Nighelli - March 26, 2015

'''

'''
Section 1
'''

# Create a dictionary containing 'name', 'city', and 'cake' for 'Chris' from 'Seattle' who likes 'Chocolate'.

dict1 = { 'name' : 'Chris',
        'city' : 'Seattle', 
        'cake' : 'chocolate'
        }

#Display the dictionary.

print 'The original dictionary: \n', dict1

#Delete the entry for 'cake'.

del dict1['cake']

#Display the dictionary.

print '\nThe dictionary missing the cake key: \n', dict1

#Add an entry for 'fruit' with 'Mango' and display the dictionary.

dict1['fruit'] = 'Mango'

# Display the dictionary keys.

print "\nThe keys in the dictionary are: ", dict1.keys()

# Display the dictionary values.

print "\nThe values in the dictionary are: ", dict1.values()

#Display whether or not 'cake' is a key in the dictionary (i.e. False) (now).

print "\nIs the key 'cake' in the dictionary anymore?"
print 'cake' in dict1

#Display whether or not 'Mango' is a value in the dictionary.

print "\nIs the value 'Mango' in the dictionary?"
print 'Mango' in dict1.values()

'''
Task 2

The dict() constructor builds dictionaries directly from sequences of key-value pairs
Convert an integer number (of any size) to a lowercase hexadecimal string prefixed with '0x'
* There is a hex function that does this! ex: hex(255)
'''
# Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).

numbers = range(16)
hexes = []
for num in numbers:
    hexes.append(hex(num))
# print zip(numbers, hexes) returns [(0, '0x0'), (1, '0x1'), (2, '0x2'), (3, '0x3'), (4, '0x4'), (5, '0x5'), (6, '0x6'), (7, '0x7'), (8, '0x8'), (9, '0x9'), (10, '0xa'), (11, '0xb'), (12, '0xc'), (13, '0xd'), (14, '0xe'), (15, '0xf')]

hex_dictionary = dict(zip(numbers, hexes))

print "\nThe number-hex dictionary: ", hex_dictionary

''' 
Task 3
'''

#Using the dictionary from item 1: Make a dictionary using the same keys but with the number of 'a's in each value.

dict_a_values = {}

for key, values in dict1.iteritems():
    dict_a_values[key] = values.count('a')

print "\nThe dictionary with the values being the number of times the letter a appears \
in the dictionary from the first task :\n", dict_a_values


'''
Task 4
'''

# Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))

# Display the sets.

print "\nSets:" 
print "s2: ", s2
print "s3: ", s3
print "s4: ", s4

# Display if s3 is a subset of s2 (False) and if s4 is a subset of s2 (True).

print "\nIs s3 a subset of s2?"
print s3.issubset(s2)

print "\nIs s4 a subset of s2?"
print s4.issubset(s2)

'''
Task 5
'''

# Create a set with the letters in 'Python' and add 'i' to the set.
pyset = set('Python')
pyset.add('i')

# Create a frozenset with the letters in 'marathon'
frozen = frozenset('marathon')

# Display the union and intersection of the two sets.
print "\nThe union of set('Pythoni') and frozenset('marathon') is : "
print pyset.union(frozen)

print "\nThe intersection of set('Pythoni') and frozenset('marathon') is : "
print pyset.intersection(frozen)

# If you reverse the union and intersection commands, the contents of the set are
# the same. However, when reversed (ie. frozen.union(pyset)), the result is a 
# frozen set. It seems like it takes on the properties of outside set. 
