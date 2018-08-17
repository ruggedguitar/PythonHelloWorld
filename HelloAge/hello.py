# This program says hello and asks for your name

print('Hello, I hope you are doing well!')
print('What is your name?')
myName = input()
print('It is very nice to meet you, ' + myName)
print('The length of your name is:')
print(str(len(myName)) + ' characters long.')
print('If you do not mind me asking, how old are you?')
myAge = input()
print('Wow, can  you believe that much time has passed? You will be ' + str(int(myAge) + 1) + ' next year!')
