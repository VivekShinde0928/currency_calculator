"""
Author  : Vivek Shinde
Date    : 23/07/2020
purpose : Practice problem solving
code    : currency calculator

"""

with open('currency.txt') as f:
    lst = f.readlines()
# print(lst)

my_dict = {}
for i in lst:
    y = i.split('\t')
    # print(y)
    my_dict[y[0]] = y[1]  # makes list to dictionary in keys & values

# print(my_dict)

print('\nAvailable currency are : ')
for key in my_dict.keys():
    print(key)

currency = input('\nPlease select the above currency : ')
amount = int(input("\nPlease enter your amount which u wanna convert: "))

z = amount * float(my_dict[currency])
print(f'\"{amount} INR equals to  {z} {currency}\"')
