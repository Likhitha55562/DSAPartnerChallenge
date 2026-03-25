
#Day - 2soloutiond

# Number even or not
num = int(input())
if num%2==0:
    print("Even")
else:
    print("Odd")

# Name as input
name = input()
print(f"Hello {name} Welcome to the DSA Challenge")

# Simple interest
P = int(input("Enter the principal amount: "))
T = int(input("Enter the time taken: "))
R= int(input("Enter the rate of interest: "))
SI = (P*T*R)/100
print(SI)


# Operations using the operators
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
oper = input("Enter the operator (+, -, *, /): ")
if oper == '+':
    res = num1 + num2
elif oper == "-":
    res = num1 - num2
elif oper == '*':
    res = num1 * num2
elif oper == '/':
    if num2 != 0:
        res = num1 / num2
    else:
        res = "Division by zero not allowed"
else:
    result = "Invalid operator"
print("Output:", res)

#Largest 
a = int(input())
b = int(input())
if a>b:
    print("Largest num is" , a)
else:
    print("Largest num is ", b)

#Indian to US conversion
amt = float(input("Enter the amount: "))
if amt>0:
    usd = amt/83.5
    print(f"{usd:.2f}")
else:
    print("Amount not valid")

#Fibonacci series
n = int(input("Number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a , end = " ")
    c = a+b
    a = b
    b = c

#Palindrome or not 
strg = input("Enter the string: ")
rev = ""
for ch in strg:
    rev = ch+rev
if rev == strg:
    print("Palindrome")
else:
    print("Not a palindrome")

#Armstrong number
num = int(input("Enter the number: "))
temp = num
order = len(str(num))
sum = 0
while num>0:
    a = num%10
    sum+=pow(a,order)
    num//=10
if sum == temp:
    print("The number is an armstrong number")
else:
    print("It is not an armstrong number")