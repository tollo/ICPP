# File management example

nameHandle = open('kids', 'w')
for i in range(2):
    name = input('Enter a name: ')
    nameHandle.write(name + '\n')
nameHandle.close()
