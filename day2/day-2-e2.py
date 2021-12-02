# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
fHeight = float(height)
iWeight = int(weight)

bmi = (float(iWeight) / (fHeight ** 2))
print(int(bmi))

