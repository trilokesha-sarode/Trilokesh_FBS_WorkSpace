# Write a program to enter P, T, R and calculate Compound Interest.
P = int(input("Enter Principle Amount : "))
R = float(input("Enter Rate of annual interest :"))
T = int(input("Enter Time Period :"))



Compound = P*((1+(R/100))**T)

Compound_interest = Compound - P

print(f' The Compound interest is {Compound_interest}')
