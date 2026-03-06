# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 23:47:22 2026

@author: Micha
"""
item = input("Enter item type (A or B): ")
quantity = float(input("Enter item quantity: "))
if item == "A":
    unit_price = 10
else: 
    unit_price = 20 

ext_price = quantity * unit_price


print()
print("Item type: ", item)
print("Quantity: ", quantity)
print("Unit price: $", unit_price)
print("Total price: $", ext_price)