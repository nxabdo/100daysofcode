# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
buyer = random.randint(0, len(names))
print(f"{names[buyer]} is going to buy the meal today!")
