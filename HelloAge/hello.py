# This program says hello, asks for your name, asks age, and reponds to it.

print('Hello, I hope you are doing well!')
print('What is your name?')
myName = input()
print('It is very nice to meet you, ' + myName)
print('The length of your name is:')
print(str(len(myName)) + ' characters long.')
print('If you do not mind me asking, how old are you?')
myAge = int(input())
if myAge > 49:
    print('HOLY COW! Can you believe that much time has passed? You will be ' + str(int(myAge) + 1) + ' next year!')
if myAge < 50:
    print('You are not THAT old! You will only be ' + str(int(myAge) + 1) + ' next year!')