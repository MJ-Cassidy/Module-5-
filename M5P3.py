# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 00:15:27 2026

@author: Micha
"""

quantity = float(input("Enter # of books you want to order: "))
p_per = float(input("Enter price per book: $"))

ppo = quantity * p_per

if ppo <= 50:
    ship_fee = 25
else:
    ship_fee = 0

total = ppo + ship_fee

print("Number of books ordered: ", quantity)
print("Price per book: $", p_per)
print("Order price: $", ppo)
print("Shipping fee: $", ship_fee)
print("Total price: $", total)