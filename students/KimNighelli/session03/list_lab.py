#!/usr/bin/env python

'''
This program highlights varies taks one can perform on a list, from appending,
removing, iterating through, and doubling. 

This program also has a raw_input option for user interation.
'''

# Create a list that contains Apples, Pear, Oranges and Peaches. Then print. 

fruits_list = ["Apples", "Pears", "Oranges", "Peaches"]
print fruits_list

# Ask the user for another fruit and add it to the end of the list. Then print.

users_fruit = raw_input("What fruit would you like me to add to this list? ")
fruits_list.append(users_fruit)

print fruits_list


# Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).

users_index = raw_input("What index would you like me to return to you? ")

print "The fruit at index %s is %s." % (users_index, fruits_list[int(users_index) - 1])


# Add another fruit to the beginning of the list using + and display the list.

fruits_list = ["Kiwis"] + fruits_list
print fruits_list


# Add another fruit to the beginning of the list using insert() and display the list.

fruits_list.insert(0, "Bananas")
print fruits_list

# Display all the fruits that begin with P, using a for loop.

for fruit in fruits_list:
    if fruit[0].lower() == "p":
        print fruit

# Using the list created in series 1 above: Display the list.
# I'm going to make a copy of fruits_list since we need it later
# I'll also be multiplying it by 2 per (Bonus: Multiply the list times two. 
# Keep asking until a match is found. Once found, delete all occurrences.)

print fruits_list

fruits_list_t2 = fruits_list * 2

# Display the list. Remove the last fruit from the list. Display the list.

print fruits_list_t2

fruits_list_t2.pop()

print fruits_list_t2

# Ask the user for a fruit to delete and find it and delete it.

print "All of the current fruits are: \n%s. Please choose one to delete. \n" % (fruits_list_t2)
fruit_to_delete = raw_input("Which fruit would you like to delete? ")

for fruit in fruits_list_t2:
    if fruit == fruit_to_delete:
        fruits_list_t2.remove(fruit)

print fruits_list_t2


# Again, using the list from series 1 (fruits_list)- make a copy
fruits_list_t3 = fruits_list[:]
print fruits_list_t3

# Ask the user for input displaying a line like Do you like apples? for each fruit in the 
# list (making the fruit all lowercase). For each no, delete that fruit from the list.
# For any answer that is not yes or no, prompt the user to answer with one of those two values 
# (a while loop is good heres). Then display.

for fruit in fruits_list:
    
    user_input = raw_input("Do you like %s? (yes/no) " % (fruit.lower()))

    while user_input.lower() != "yes" and user_input.lower() != "no":
        print "Please enter a valid input of 'yes' or 'no'"
        user_input = raw_input("Do you like %s? (yes/no) " % (fruit.lower()))

    if user_input.lower() == "no":
        fruits_list_t3.remove(fruit)
        print "removed %s from list" % (fruit)

print fruits_list_t3


# Once more, using the list from series 1: Make a copy of the list and reverse 
# the letters in each fruit in the copy. Delete the last item of the original list. 
# Display the original list and the copy

fruits_list_t4 = fruits_list[:]

for fruit in fruits_list_t4:
    fruit = fruit[::-1]

print fruits_list_t4

'''
When the script is run, it should accomplish the following four series of actions:


    Make a copy of the list and reverse the letters in each fruit in the copy.
    Delete the last item of the original list. Display the original list and the copy
'''
