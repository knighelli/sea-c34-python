'''
This is for Task 7- Planning Mailroom Madness

This "program" is simply a program outline to help me plan how
I'm going to code up the Mail Room Madness task. I also wrote an
outline that I attached to the homework submission.

Obviously, this program will not run- that's next session's task!

There seem to be three major blocks that I'll split up into their own
separate functions:
    1) The initial selection
    2) What to do when you want to send a thank you
    3) What to do when you want a donor report

'''

# First I'd like to create a donor database. The value in the key-value
# pair will be a list since a donor can donate more than once.

donor_db = { "Patti Guenard" : [457.00, 54.36, 100.00],
        "Lynn Ellis" : [84.00, 12.86, 90.00],
        "Tedrick Mealy" : [1000.00],
        "Jeff Lerner" : [400.00, 500.00, 20.00]
        }

# The following will be the "choose what you want to do" function:

def initial_choice():

    '''
    Ask the user what they want to do via terminal
    '''

    choice = raw_input("What would you like to do? Choose 'A' to send a thank you, "
            "choose 'B' to print a donor report, or choose 'C' to quit the program")

    return choice

def send_thank_you():
    '''
    The user enters this loop if they choose A above

    First ask the user what they want to do
    '''

    name = raw_input("What donor, new or existing, would you like to work with? "
            "You can also type 'list' here to receive a list of previous donors or "
            "you can type 'quit' to exit the program")


    # I'll probably put this in a while loop since I have to reprompt after listing donors
    if name == 'list':
        print "Donors who have previously donated are:"
        for donor in donor_db:
            print donor
        reprompt the raw_input
    elif name == 'quit':
        quit the program

    # Add donor to db if they're not in there
    if name not in donor_db:
        donor_db[name] = []

   # Ask how much the person donated

   amount = raw_input("How much did %s donate? You can also type 'quit' here to "
           "exit the program" % (name))

   if amount == 'quit':
       exit the program
   else:
       donation_amount = float(amount)

   # Do some test on donation amount to make sure it's an actual number, float, etc
   # I may want to check if the donation amount > 0. 
   # I'd then print something to tell the user that the amount is invalid
   # and return to the amount raw_input. (**** while loop?)

   # Add amount to database (the amounts are in a list- append)
   donor_db[name].append(donation_amount)

   # Print email to terminal

   print "Dear %s, thank you very much for your donation of %f" % (name, donation_amount)



# Below is the function to print a donor report

def print_report():

    '''
    First, I'll need to calculate the sum of the donations, the number of donations, and the
    average donation for each donor. I'l probably append it all to a list
    '''

    metrics = []
    for (name, donations) in donor_db.items():
        calculate total
        calculate number 
        calculate average
        append name, total, number, average to metrics

    '''
    Next, I need to display the metrics in tabular form. I'll need to look up how to do this
    '''

    for items in metrics:
        print it like a table

    '''
    Allow the user to return to the original prompt
    '''


'''
THINGS TO IMPLEMENT

I'll need to figure out a way to actually take the selection from the "what do you want to do"
section and make it run the correct function. Functions can be called in the if __name__ = 
"__main__" loop- I might do something there. Don't know what yet. 

I forsee struggles with the instruction to allow the user to return to the original prompt.

Print the data to a table for the report will be difficult. 

'''
