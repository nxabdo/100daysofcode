# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#Anegla would cast here
column =(position[0:1])
row = (position[1:len(position)])

#Angelas way much simpler no if statements
#I don't case but angela casts
# map[column-1][row-1] ="X"

if (row == '1'):
    if (column == '1'):
        row1[0] = 'X'
    elif (column == '2'):
        row1[1] = 'X'
    elif (column == '3'):
        row1[2] = 'X'
    else:
        print("Invalid input!")

elif (row == '2'):
    if (column == '1'):
        row2[0] = 'X'
    elif (column == '2'):
        row2[1] = 'X'
    elif (column == '3'):
        row2[2] = 'X'
    else:
        print("Invalid input!")

elif (row == '3'):
    if (column == '1'):
        row3[0] = 'X'
    elif (column == '2'):
        row3[1] = 'X'
    elif (column == '3'):
        row3[2] = 'X'
    else:
        print("Invalid input!")

else:
    print("Invalid input!")

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")