#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
billTotal = input("What was the total bill? ")
tipInput = input("How much tip would you like to give? 10, 12, or 15? ")
totalPpl = input("How many people to split the bill? ")

bill = float(billTotal)
tip = float(tipInput)
ppl = float(totalPpl)

tipPerPerson =  (bill * (tip / 100))/ppl
billPerPerson = (bill / ppl)
toalPerPerson = (tipPerPerson + billPerPerson)
roundedTotal = round(toalPerPerson, 2)

print(f"Each person should pay: ${roundedTotal}")