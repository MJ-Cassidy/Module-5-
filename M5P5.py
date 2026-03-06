# -*- coding: utf-8 -*-
"""
Created on Sat Feb 28 01:03:53 2026

@author: Micha
"""

name = input("Enter last name: ")
dependants = float(input("Enter number of dependants: "))
gi = float(input("Enter gross income: $"))

adj_gi = gi - (dependants * 12000)

if adj_gi <= 50000:
    tax_rate = .1
else:
    tax_rate = .2
    
inc_tax = adj_gi * tax_rate

if inc_tax <= 0:
    inc_tax = 100
    
print()
print(name)
print()
print("Gross income: $", gi)
print("Number of dependants: ", dependants)
print("Adjusted gross income: $", adj_gi)
print("Income tax: $", inc_tax)