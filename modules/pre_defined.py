#Module - Pre-Defined

#math
import math
print("\n")
print("Imported math module")
print("---------------------")
print("Printing pi      : ", math.pi)
print("Printing sin(90) : ", math.sin(1))
print("Printing cos(90) : ", math.cos(1))
print("Printing tan(90) : ", math.tan(1))
print("Printing 3!      : ", math.factorial(3))
print("\n")

#random
from random import randrange, choice, random
print("Imported random module")
print("-----------------------")
randomlist = ["A", 1, 86.50,[1,2,3],"Hello World!"]
print("Random Range: 1 to 10")
print("Printing a random number from 1 to 10 : ",randrange(1,10+1))
print("\n")

print("Random Choice:")
print("List used for random pick : ",randomlist)
print("Picking a random entity from the list : ",choice(randomlist))
print("\n")

print("Random:")
print("Printing a random number : ",random())
print("\n")

#fraction
from fractions import Fraction as a
print("Imported fractions module")
print("-------------------------")
deci2=float(input("Enter a decimal value : "))
print("Fraction for ",deci2," is : ",a(deci2))
print("\n")

numerator=int(input("Provide a numerator for the fraction : "))
denominator=int(input("Provide a denominator for the fraction : "))
print("Fraction is : ",a(numerator, denominator))
print("Adding given number with 1/2 is : ",a(1,2)+a(numerator, denominator))
print("\n")

#decimal
import decimal
print("Imported decimal module")
print("-------------------------")
deci1=float(input("Provide a decimal number : "))
print(decimal.Decimal(deci1))
print("\n")
