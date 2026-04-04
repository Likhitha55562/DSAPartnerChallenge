
# Day - 17 Solutions

# Fibonacci number
def fibona(n):
    if n<2:
        return n
    return fibona(n-1)+fibona(n-2)
print(fibona(3))

# Special Fibonacci
def spe_fib(a,b,n):
    if n<2:
        return n
    for _ in range(2,n+1):
        a,b = b,a+b
    return b
print(spe_fib(2,3,5))

# Length of string
def len_str(s,i=0):
    if len(s) == i:
        return 0
    return 1+ len_str(s,i+1)
print(len_str("Hello",0))

# Geek-onacci Number
def geek_num(n):
    if n<=3:
        return 1
    a,b,c= 1,1,1
    for _ in range(4,n+1):
        d = a+b+c
        a,b,c= b,c,d
    return c
print(geek_num(4))

# Recursive Bubble Sort 
def recur_bubble(arr,n):
    if n==1:
        return 
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    recur_bubble(arr,n-1)
arr = [3,2,5,1,4]
recur_bubble(arr,len(arr))
print(arr)

# Recursive Insertion Sort 
def recurs_ins(arr,n):
    if n<=1:
        return
    recurs_ins(arr,n-1)
    key = arr[n-1]
    j = n-2
    while j>=0 and arr[j]>key:
        arr[j+1]= arr[j]
        j-=1
    arr[j+1] = key
arr = [5, 3, 2, 4, 1]
recurs_ins(arr, len(arr))
print(arr)

# Sum of digits
def sum_dig(n):
    if n==0:
        return 0
    return n%10 + sum_dig(n//10)
print(sum_dig(123))

# Product of two numbers
def pro(a,b):
    if b==0:
        return 0
    return a + pro(a,b-1)
print(pro(2,3))

# Check Prime using Recursion
import math
def check_prime(n,div=2):
    if n<2:
        return False
    if div>int(math.sqrt(n)):
        return True
    if n%div == 0:
        return False
    return check_prime(n,div+1)
print(check_prime(2))

# Sum of Natural Numbers using Recursion
def sum_of_num(n):
    if n==0:
        return 0
    return n + sum_of_num(n-1)
print(sum_of_num(3))