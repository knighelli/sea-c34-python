'''
This is for Task 15: Lambda and Keyword Argument Magic

Write a function that returns a list of n functions, such that each one,
when called, will return the input value, incremented by an increasing number.

Use a for loop, a lambda, and a keyword argument

( Extra credit ): Do it with a list comprehension, instead of a for loop

Kimberlee Nighelli - 31 March 2015
'''

# For Loop


def func(x, i=0):
    return x + i


def function_builder(n):
    '''
    This function returns a list of n functions such that each one,
    when called, will return the input value, incremented by an
    increasing number.
    '''
    a_list = []
    for i in range(n):
        a_list.append(lambda x, p=i: x+p)
    return a_list


def function_builder_lc(n):
    '''
    Does the same as above w/ a list comp
    '''
    a_list = [lambda x, p=i: x+p for i in range(n)]

if __name__ == "__main__":
    a_list = function_builder(10)
    print a_list[5](3)
