# Sums the numbers in a string

string = '1.23,2.4,3.123'
string_list = string.split(',')
float_list = [float(i) for i in string_list]

total = 0

for i in float_list:
    total = total + i

print(total)

