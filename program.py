# PYTHON PROGRAM TO GENERATE VALUE OF π

#Import from  library
import math
print("The Value of π is", math.pi)

# Programme to find the volume of sphere

import math
π = math.pi
R = 50 #Radias of the sphere is 50 cm
V = (4/3) * π * R * R * R  #V=volume of sphere
print("Volume of the given sphere ", V )

# Programme to find Area of Circle

import math
π = math.pi
r = 27
A = π*r*r
print (" Area of the given circle is" ,A)

# Programme to find the Area of a square



import math
side = float (input("Enter Value of side of the aquare:"))
A = side*side
print(" Area of the square is", A)

# Program to find the Sum and average of a list of numbers

n=int(input("Enter the number of list: "))
a=[]
for i in range(0,n):
    list=int(input("Enter list: "))
    a.append(list)
    s=sum(a)
    avg=sum(a)/n
print("Sum of the list of numbers is  ", s)
print("Average of elements in the list is ",avg)
