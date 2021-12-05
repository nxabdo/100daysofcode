for i in range (0,101, 1):
    if (i%3==0):
        print("Fizz\n")
    elif (i%5==0):
        print("Buzz\n")
    elif (i%5==0 and i%3==0):
        print("FizzBuzz\n")
    else:
        print(str(i) +"\n")