SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(num_tickets):
    return (num_tickets * TICKET_PRICE) + SERVICE_CHARGE


while tickets_remaining >= 1: 
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?  ")
    number_of_tickets = input("Hello, {}! How many tickets would you like to buy?  ".format(name))
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("Sorry, there are only {} tickets remaining.".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue {}.  Please try again".format(err))
    else:
        total_price = calculate_price(number_of_tickets)
        print("Thanks a lot,", name.title(), "! The total price for", number_of_tickets, "tickets is", total_price, ".")
        confirm_cart = input("Would you like to proceed?  Please enter y/n  ")
        if confirm_cart.lower() == "y":
            # TODO: Gather credit card information and process it.
            print("SOLD")
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you for your time.  Have a wonderful day, {}!".format(name))
print("Sorry, there are no more tickets left :(")
