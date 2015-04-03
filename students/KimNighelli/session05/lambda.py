'''
This is for Task 15: Lambda and Keyword Argument Magic

Write a function that returns a list of n functions, such that each one,
when called, will return the input value, incremented by an increasing number.

Use a for loop, a lambda, and a keyword argument

( Extra credit ): Do it with a list comprehension, instead of a for loop

Kimberlee Nighelli - 31 March 2015
'''

# For Loop


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
    This function returns a list of n functions such that each one,
    when called, will return the input value, incremented by an
    increasing number. This function, unlike the first, completes
    this task with a list comprehension.
    '''
    a_list = [lambda x, p=i: x+p for i in range(n)]
    return a_list

'''
Testing
'''

if __name__ == "__main__":

    a_list = function_builder(10)

    assert a_list[5](3) == 8
    assert a_list[9](12) == 21
    assert a_list[0](4) == 4

    a_list = function_builder(3)

    assert a_list[1](2) == 3
    assert a_list[2](0) == 2

    a_list_lc = function_builder_lc(10)

    assert a_list_lc[5](3) == 8
    assert a_list_lc[3](2) == 5

    a_list_lc = function_builder_lc(5)

    assert a_list_lc[4](2) == 6
    assert a_list_lc[1](1) == 2

    print "All tests passed"
