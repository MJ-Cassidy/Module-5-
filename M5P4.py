# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 00:57:43 2026

@author: Micha
"""

name = input("Enter name of appliance: ")
price = float(input("Enter price of appliance: $"))

if price >= 1000:
    warranty = price * .1
else: 
    warranty = price * .05

total = price + warranty

print()
print(name)
print("Price of appliance: $", price)
print("Price of warranty: $", warranty)
print("Total price: $", total)