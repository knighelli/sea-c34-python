'''
This is for Task 11- Mailroom Madness


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
            "choose 'B' to print a donor report, or choose 'C' to quit the program\n\n")

    return choice

def get_name():
    while True:
        name = safe_input("\nWhat donor, new or existing, would you like to work with? "
            "You can also type 'list' here to receive a list of previous donors or "
            "you can type 'quit' to exit the program: ")

        if name.lower() == 'list':
            print "Donors who have previously donated are:"
            for donor in donor_db:
                print "   ", donor
        else:
            return name


def send_thank_you():
    '''
    The user enters this loop if they choose A above
    First ask the user what they want to do
    '''
    name = get_name()

    if name == "quit":
        return

    # Ask how much the person donated

    while True:
        amount = safe_input(
            "How much did %s donate? You can also type 'quit' here to "
            "exit the program: " % (name))

        if amount.lower() == 'quit':
            return

        try:
            amount = float(amount)
        except ValueError:
            print "%s is not a valid number. Please re-enter the amount." % (amount)
            continue

        if amount <= 0:
            print "Amount donated must be greater than 0."
        else:
            break

    # Add donor to db if they're not in there
    if name not in donor_db:
        donor_db[name] = []
    donor_db[name].append(amount)

    # Print email to terminal
    print "Dear %s, thank you very much for your donation of %f" % (name, amount)



def print_report():

    '''
    First, I'll need to calculate the sum of the donations, the number of donations, and the
    average donation for each donor. I'l probably append it all to a list
    '''

    metrics = []

    header = ("Name", "Total Donations", "Number of Donations", "Average Donation")
    max_name_length = len(header[0])
    max_total_length = len(header[1])
    max_length_length = len(header[2])
    max_average_length = len(header[3])

    for (name, donations) in donor_db.items():
        total = sum(donations)
        length = len(donations)
        average = (total / length)

        metrics.append((name, total, length, average))

        max_name_length = max(len(name), max_name_length)
        max_total_length = max(len("%.02f" % (total)), max_total_length)
        max_length_length = max(len(str(length)), max_length_length)
        max_average_length = max(len("%.02f" % (average)), max_average_length)

    widths = (max_name_length, max_total_length, max_length_length, max_average_length)

    header_row = print_row(header, widths)
    seperator = "-" * len(header_row)
    print seperator
    print header_row
    print seperator
    

    for metric in metrics:
        name_string = metric[0]
        total_string = "%.02f" %(metric[1])
        length_string = "%d" %(metric[2])
        average_string = "%.02f" %(metric[3])
        row = (name_string, total_string, length_string, average_string)
        print print_row(row, widths)

    print seperator

def print_value(value, max_length):
    return value + " "*(max_length - len(value))

def print_row(row, widths):
    
    name = print_value(row[0], widths[0])
    total = print_value(row[1], widths[1])
    length = print_value(row[2], widths[2])
    average = print_value(row[3], widths[3])

    return "| %s | %s | %s | %s |" % (name, total, length, average)


def safe_input(prompt):
    try:
        return raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None


def get_choice():
    choice = ''

    while choice.lower() != "c":
        choice = initial_choice()

        if choice.lower() == "a":
            send_thank_you()
        elif choice.lower() == "b":
            print_report()

if __name__ == "__main__":
    get_choice()

