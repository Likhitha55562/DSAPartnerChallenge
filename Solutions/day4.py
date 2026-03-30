#Day - 4 Solutions

# Perimeter of rectangle
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
per = 2 * (length+breadth)
print(f"The perimeter is : {per:.2f}")

# Perimeter of square
side = float(input("Enter the side: "))
per = 4 * side
print(f"The perimeter is : {per:.2f}")

# Perimeter of rhombus
side = float(input("Enter the side: "))
per = 4 * side
print(f"The perimeter is : {per:.2f}")

# Volume of prism
base_area = float(input("Enter the base area: "))
height = float(input("Enter the height: "))
print(f"Volume of prism is : {base_area*height:.2f}")

# Volume of cylinder
import math
radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
print(f"Volume of cylinder is : {(math.pi)* radius **2 * height:.2f}")

# Volume of sphere
import math
radius = float(input("Enter the radius: "))
print(f"Volume of sphere is : {(4/3) *(math.pi)* radius **3:.2f}")

# Volume of pyramid
base_area = float(input("Enter the base area: "))
height = float(input("Enter the height: "))
print(f"Volume of pyramid is : {(1/3) * base_area * height:.2f}")

# Curved surface area of cylinder
import math
radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))
print(f"The curved surface area is : {2* math.pi * radius * height:.2f}")

# Total surface area of cube
side = float(input("Enter the length: "))
print(f"Total surface area is : {6 *  side ** 2:.2f}")

# Fibonacci series
term = int(input("The fibonacci series till term : "))
a = 0
b = 1
for i in range(term):
    print(a, end = " ")
    c = a+b
    a = b
    b = c

# Difference in product and add of digits
num = int(input("Enter the number: "))
product = 1
sum = 0
while num>0:
    digit = num%10
    product*=digit
    sum+=digit
    num//=10
difference = product-sum
print("The difference is : ", difference)
