# Iteration through a string
"""
i = 0

for i in "abcdefghij":
    i = int(input(i))
"""
d={}
for x in range(1,11):
    d['Integer_{0}'.format(x)]=int(input('Integer_' + str(x) + ':'))

print(d['Integer_5'])


