# Iteration through a string




d={}
for x in range(1,11):
    d['Integer_{0}'.format(x)]=int(input('Integer_' + str(x) + ':'))

for x in range(1,11):
    print(d['Integer_{0}'.format(x)])


print(d['Integer_5'])


