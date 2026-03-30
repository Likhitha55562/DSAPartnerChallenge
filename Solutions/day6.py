
# Day - 6 solutions

# Prime or not
import math
def is_prime(a):
    if a <=1:
        return False
    if a== 2:
        return True
    if a%2==0:
        return False
    for i in range(3,int(math.sqrt(a))+1,2):
        if a % i ==0:
            return False
    return True
print(is_prime(1))

# Grade calculator
def grade_calculator(m):
    if m>=91:
        return "AA"
    elif m>=81:
        return "AB"
    elif m>=71:
        return "BB"
    elif m>=61:
        return "BC"
    elif m>=51:
        return "CD"
    elif m>=41:
        return "DD"
    else:
        return "Fail"
print(grade_calculator(23))

# Factorial of a number
def factorial(a):
    if a == 0 or a == 1:
        return 1
    result = 1
    for i in range(2,a+1):
        result*=i
    return result
print(factorial(0))

# Palindrome or not
def is_palindrome(n):
    if n<0:
        return False
    return str(n)==str(n)[::-1]
print(is_palindrome(1221))

# Area of circle
import math
def areaOfcircle(r):
    return math.pi * ( r ** 2)
print(areaOfcircle(2))

# Perimeter of rectangle
def per_of_rec(a,b):
    return 2 * (a+b)
print(per_of_rec(2,3))

# Simple Interest
def simple_interest(principal,time,rate_of_interest):
    return (principal*time*rate_of_interest) / 100
print(simple_interest(1000,2,2))

# Pythagorean triplet
def pythagorean_triplet(a,b,c):
    nums = sorted([a,b,c])
    return nums[0] ** 2 + nums[1] ** 2== nums[2] ** 2
print(pythagorean_triplet(8,6,10))

# Prime numbers in a range
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# All Primes Between Two Numbers
def prime_in_range(start,end):
    return [n for n in range(start,end+1) if is_prime(n)]
print(prime_in_range(2,15))

# Sum of 'N' natural numbers
def sum_numbers(n):
    return n*(n+1)//2
print(sum_numbers(2))

