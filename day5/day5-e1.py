# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
totalHeights = 0
totalStudents = 0
#Write your code below this row 👇

#Sums heights of all students
for students in student_heights:
  totalHeights += students

#Sums the number of students
for students in student_heights:
  totalStudents += 1

avg = totalHeights/(totalStudents)
print(round(avg))