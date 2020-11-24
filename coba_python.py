# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 05:02:20 2020

@author: ASUS
"""

one = 1
two = 2
some_number = 12030

true_boolean = True
false_boolean = False

my_name = 'Mega'
print(my_name)

pen_price = 12.892

if True:
    print ("Hello Python If")
    
if 1>4:
    print("1 is greater than 4")
elif 4>1:
    print("1 is less than 4")
else:
    print("1 is equal to 4")
    
num = 0.5
while num<=10:
    num=num+1
    print(num)
    
for i in range(1,11,2):
    print(i)

my_columns = [3, 6, 1, 0, 2]
print(my_columns[0], my_columns[3])

dictionary_tk = {
"name": "Leandro",
"nickname": "Tk",
"nationality": "Brazilian"
}
 
print("My name is %s" %(dictionary_tk["name"]))