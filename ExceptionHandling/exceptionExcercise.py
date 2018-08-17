#This small application is an excercise to demonstratoe how to handle errors.
def math(devideBy):
    return 42 / devideBy
#try is the first step in handling errors.
try:  
    print(math(2))
    print(math(12))
    print(math(0))

#except is the second portion of the exception process.
except ZeroDivisionError:
    print('Error: Invalid Argument')