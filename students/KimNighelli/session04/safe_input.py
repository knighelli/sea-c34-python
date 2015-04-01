'''
This is for Task 10- Improving Raw Input

In this program, I create a function, safe_input() which will
modify the potential output of the raw_input() function. The
raw_input() function can generate two exceptions, either an
EOFError of a KeyboardInterrupt. The safe_input() function
will return a none rather than raising those excpetions.

Kimberlee Nighelli - 28 March 2015
'''


def safe_input(prompt):
    '''
    This function modifies the output of the
    raw_input function to return None in lieu
    of an EOFError or KeyboardInterrupt
    '''

    try:
        return raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None


safe_input("Hi")
