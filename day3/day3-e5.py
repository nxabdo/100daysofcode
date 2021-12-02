name1 = input("Please enter a name: ")
name2 = input("Please enter a second name: ")

nameConcat =  (name1 + name2).lower()
nameList = list(nameConcat)
countTrue = 0
countLove = 0

for i in range (0, len(nameList), 1):
    if nameList[i] == 't' or nameList[i] == 'r' or nameList[i] == 'u' or nameList[i] == 'e':
        countTrue += 1
    if nameList[i] == 'l' or nameList[i] == 'o' or nameList[i] == 'v' or nameList[i] == 'e':
        countLove += 1

strCountTrue = str(countTrue)
strCountLove = str(countLove)

total =  strCountTrue + strCountLove

result = int(total)

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result > 40 and result < 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")
