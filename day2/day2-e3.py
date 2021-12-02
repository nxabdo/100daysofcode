# 1 year = 365 days
# = 52 weeks
# = 12 months
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

iAge = int(age)
print(iAge)

totalDays= 90 * 365
totalWeeks =  90 * 52
totalMonths = 90 * 12

daysLived = iAge * 265
weeksLived = iAge * 52
monthsLived = iAge * 12

daysRemaining = totalDays - daysLived
weeksRemaining = totalWeeks - weeksLived
monthsRemaining = totalMonths - monthsLived

print("You have " + str(daysRemaining) + " days remaining, " + str(weeksRemaining)+ " weeks remaining," + " and " + str(monthsRemaining)+ " months remaining.")