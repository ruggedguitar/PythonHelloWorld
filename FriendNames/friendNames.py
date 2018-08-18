#This application organizes and displays a friends list entered by the user
friendNames = []
while True:
    print('Enter the name of your best friend ' + str(len(friendNames) + 1) +
        ' (Once you are finished typing your friends list, simply push enter.)')
    name = input()
    if name == '':
        break
    friendNames = friendNames + [name] # list concatenation
print('Your friends list is as follows:')
for name in friendNames:
    print(' ' + name)