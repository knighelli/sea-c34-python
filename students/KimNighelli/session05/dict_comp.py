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
                 "age": 24,
                 "fruit": "apples",
                 "animal": "manatees",
                 "cloud": "mammatus",
                 "activity": "spinning",
                 "dream_activity": "sleeping"
                 }

# Print the dict by passing it to a string format method

print "{name} is {age}. Her favorite fruit are {fruit} and her favorite" \
      "animals are {animal}. Because she's a meteorologist, her" \
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
