size = input("What size would you like to order? ")
bill = 0
add_pep = input("Would you like to add pepperoni? ")
extra_cheese = input("Would you like extra cheese? ")

if size == 'S':
    bill = 15
    if add_pep == 'Y':
        bill = bill + 2
    elif add_pep == 'N':
        bill = bill

elif size == 'M':
    bill = 20
    if add_pep == 'Y':
        bill = bill + 3
    elif add_pep == 'N':
        bill = bill

elif size == 'L':
    bill = 25
    if add_pep == 'Y':
        bill = bill + 3
    elif add_pep == 'N':
        bill = bill

if extra_cheese == 'Y':
    bill = bill + 1
elif extra_cheese == 'N':
    bill = bill

print(f"Your final bill comes out to ${bill}")
