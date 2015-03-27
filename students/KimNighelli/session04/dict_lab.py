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

print "\n The keys in the dictionary are: ", dict1.keys()

# Display the dictionary values.

print "\n The values in the dictionary are: ", dict1.values()
'''
Display the dictionary keys.
Display the dictionary values.
Display whether or not 'cake' is a key in the dictionary (i.e. False) (now).
Display whether or not 'Mango' is a value in the dictionary.
Using the dict constructor and zip, build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent (string is fine).
Using the dictionary from item 1: Make a dictionary using the same keys but with the number of 'a's in each value.
Create sets s2, s3 and s4 that contain numbers from zero through twenty, divisible 2, 3 and 4.
Display the sets.
Display if s3 is a subset of s2 (False)
and if s4 is a subset of s2 (True).
Create a set with the letters in 'Python' and add 'i' to the set.
Create a frozenset with the letters in 'marathon'
display the union and intersection of the two sets.

'''
