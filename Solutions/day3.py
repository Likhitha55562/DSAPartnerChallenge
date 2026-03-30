
#Day - 3 solutions

#Area of circle
import math
r= float(input("Enter the radius: "))
area = math.pi * r **2
print(f"The area is:  {area:.2f}")

#Area of traingle
base= int(input("Enter the base : "))
height = int(input("Enter the height: "))
area = 0.5*base*height
print(f"The area is {area:.2f}")

#Area of rectangle
l= float(input("Enter the length : "))
b = float(input("Enter the breadth: "))
area = l * b
print(f"The area is {area:.2f}")

#Area of  isoceles traingle
b= int(input("Enter the base : "))
h = int(input("Enter the height: "))
area = 0.5*b*h
print(f"The area is {area:.2f}")

#Area of parallelogram
b = float(input("Enter the base: "))
h = float(input("Enter the height: "))
area = l*h
print(f"The area is {area:.2f}")

#Area of rhombus
d1= float(input("Enter the diagonal1 : "))
d2 = float(input("Enter the diagonal2: "))
area = 0.5*d1*d2
print(f"The area is {area:.2f}")

#Area of equilateral
import math
side = int(input("Enter the side: "))
area = (math.sqrt(3) / 4) * side ** 2
print(f"The area is : {area:.2f} ")

#Perimeter of circle
import math
r = int(input("Enter the radius: "))
per =  (math.pi) * 2 * r
print(f"The perimeter is: {per:.2f}")

#Perimeter of equilateral trinagle
side = int(input("Enter the side: "))
per = 3 * side
print(f"The perimeter is {per:.2f}")

#Perimeter of parallelogram
a = int(input("Enter the side: "))
b = int(input("Enter the other side: "))
per = 2 * (a+b)
print(f"The perimeter is {per:.2f}")

