'''
This is for Task 10- Improving Raw Input. 

In this program, I create a function, safe_input() which will 
modify the potential output of the raw_input() function. The
raw_input() function can generate two exceptions, either an
EOFError of a KeyboardInterrupt. The safe_input() function 
will return a none rather than raising those excpetions. 

Kimberlee Nighelli - 28 March 2015
'''

def safe_input(x):
    try:
        user_input = raw_input(x)
    except EOFError, KeyboardInterrupt:
        return None

    return user_input

