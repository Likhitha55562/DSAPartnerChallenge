
# Day - 5 Solutions


# Palindrome or not
def is_palindrome(num):
    temp = num
    rev = 0
    while num>0:
        a = num%10
        rev = rev*10 + a
        num//=10
    if temp == rev:
        print("IS A PALINDROME")
    else:
        print("Not a palinrome")

is_palindrome(121)

# HCF and LCM two numbers
def hcf_lcm(a,b):
    x,y = a,b
    while b!=0:
        a , b = b, a%b
    print(a)
    lcm = (x*y)//a
    print(lcm)
hcf_lcm(6,12)

# Vowel or consonant
def check_vowel(a):
    arr = ['a','e','i','o','u']
    if a in arr:
        print("It is a vowel")
    else:
        print("Not an vowel")

check_vowel('a')

# Perfect number
def perfect_num(a):
    c = 0
    for i in range(1,a//2+1):
        if a%i==0:
            c+=i
    if c == a:
        print("It is a perfect number")
    else:
        print("Not a perfect number")
perfect_num(6)

# Leap year
def leap_year(yr):
    if yr%400==0 or (yr%4==0 and yr%100!=0):
        print("It is a leap year")
    else:
        print("It is not a leap year")
leap_year(2010)

# Sum of digits of a number
def sum_of_digits(a):
    sum_is = 0
    while a > 0:
        sum_is +=a%10
        a//=10
    return sum_is
print(sum_of_digits(123))

# Even days
def even_days(a):
    count = 0 
    for i in range(1,a+1):
        if i%2==0:
            count+=1
    return count
print(even_days(31))

# Sum of different numbers
def sum_of_num(arr):
    neg_sum = 0
    pos_num_odd = 0
    pos_num_even = 0
    for val in arr:
        if val<0:
            neg_sum+=val
        elif val%2==0:
            pos_num_even+=val
        else:
            pos_num_odd+=val
    return neg_sum, pos_num_even, pos_num_odd
print(sum_of_num([2,5,9,3,-3,-1,2,-4]))

# Max and min
def max_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(max_num(5,2,1))

def min_num(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c   
a = int(input("The first number: "))
b = int(input("The second number: "))
c = int(input("The third number: "))
print(min_num(a,b,c))
print(max_num(a,b,c))

# Even or odd number
def even_odd(a):
    if a%2==0:
        print("It's an even number")
    else:
        print("It's an odd number")
even_odd(5)

# Voting eligiblity
def eligibilty(age):
    return age>=18
print(eligibilty(12))

# Sum of 2 numbers
def sum_num(a,b):
    return a + b
print(sum_num(3,2))

# Sum of "N" numbers
def sum_of_num():
    total = 0
    while True:
        num = int(input("Enter the number: "))
        if num ==0:
            break
        else:
            total+=num
    return total
print(sum_of_num())
