# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 13:30:37 2026

@author: Micha
"""

quantity = float(input("enter quantity of units you would like to purchase: "))

if quantity >= 1000:
    price_per_unit = 3
else: 
    price_per_unit = 5
    
ext_price = quantity * price_per_unit 

tax = ext_price * .07

final_price = ext_price + tax

print("Quantity: ", quantity)
print("Price per unit: $", price_per_unit)
print("Extended price: $", ext_price)
print(f"Tax: $ {(tax): .2f}")
print("Final price: $", final_price)