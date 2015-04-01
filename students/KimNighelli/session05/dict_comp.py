'''
This is for Task 14- Dictionary and Set Comprehensions

This assingment revists some of the tasks we complete in the original
dict/set lab. In this assignment, we will attempt to complete those tasks
with list comprehensions

Each individual subtask/question will be noted with a comment '#'

Kimberlee Nighelli - 31 March 2015
'''

# Create an about me dictionary for subtask 1

about_me_dict = {"name": "Kimberlee Nighelli",
                 "hometown": "Haverhill, Mass",
                 "fruit": "apples",
                 "animal": "manatees",
                 "cloud": "mammatus",
                 "activity": "spinning",
                 "dream_activity": "sleeping"
                 }

# Print the dict by passing it to a string format method

print "{name} is from {hometown}. Her favorite fruit are {fruit} and her" \
      "favorite animals are {animal}. Because she's a meteorologist, her" \
      "favorite clouds are {cloud} clouds (they're indicative of " \
      "severe weather!). In her spare time, Kim enjoys {activity} " \
      "but would rather be {dream_activity} most of the " \
      "time!\n".format(**about_me_dict)

# Using a list comprehension, build a dictionary of numbers from zero to
# fifteen and the hexadecimal equivalent (string is fine).

numbers = range(16)
hexes = [hex(i) for i in numbers]
hex_dict = dict(zip(numbers, hexes))
print hex_dict

# Do the previous entirely with a dict comprehension, should be a one-liner

hex_dict_dc = {i: hex(i) for i in numbers}
print hex_dict_dc

print hex_dict == hex_dict_dc

# Using the dictionary from item 1: Make a dictionary using the same keys
# but with the number of 'a's in each value. You can do this either by
# editing the dict in place, or making a new one. If you edit in place,
# make a copy first!

a_about_me_dict = {key: values.count('a') for key, values in
                   about_me_dict.items()}

print a_about_me_dict

# Create sets s2, s3 and s4 that contain the numbers from zero through
# twenty that are divisible 2, 3 and 4.
# a. Do this with one set comprehension for each set.

s2 = {i for i in range(21) if i % 2 == 0}
s3 = {i for i in range(21) if i % 3 == 0}
s4 = {i for i in range(21) if i % 4 == 0}

print s2
print s3
print s4

# create a sequence that holds all three sets
# loop through that sequence to build the sets up so no repeated code.

s2, s3, s4 = [{i for i in range(21) if i % j == 0} for j in range(2, 5)]

print s2
print s3
print s4
