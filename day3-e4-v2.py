size = input("What size would you like to order? ")
bill = 0
add_pep = input("Would you like to add pepperoni? ")
extra_cheese = input("Would you like extra cheese? ")

if size == 'S':
    bill += 15

elif size == 'M':
    bill += 15
else:
    bill += 25

if add_pep == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1


print(f"Your final bill comes out to ${bill}")
