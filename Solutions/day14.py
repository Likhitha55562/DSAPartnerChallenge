# Day - 14 Solutions

# Square pattern
for i in range(5):
    for j in range(5):
        print("*",end = " ")
    print()

# Right triangle
for i in range(5):
    for j in range(0,i+1):
        print("*",end= "")
    print()

# Inverted triangle
for i in range(5,0,-1):
    for j in range(i):
        print("*",end= "")
    print()

# Number triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end= " ")
    print()

# Diamond/Rhombus(left-aligned)
for i in range(5):
    for j in range(0,i+1):
        print("*",end= "")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print("*",end= "")
    print()

# Right-aligned triangle
n=5
for i in range(1,6):
    print(' '*(n-i)+ "*"*i)

# Inverse Right-aligned triangle
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
   
# Pyramid (Centered)
n=5
for i in range(1,n+1):
    print(' '*(n-i)+ '*'*(2*i-1))

# Inverted pyramid
n = 5
for i in range(5,0,-1):
    print(' '*(n-i)+ '*'*(2*i-1))

# Butterfly
n = 5
for i in range(1,n+1):
    for j in range(i):
        print("*",end = "")
    for j in range(2*(n-i)):
        print(' ',end = "")
    for j in range(i):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end = "")
    for j in range(2*(n-i)):
        print(' ',end = "")
    for j in range(i):
        print("*",end="")
    print()

# Hollow rectangle 
r,c = 4,4
for i in range(r):
    for j in range(c):
        print("*" if i==0 or i == r-1 or j==0 or j==c-1 else ' ',end='')
    print()

# Number Staircase
n = 1
for i in range(5):
    for j in range(0,i+1):
        print(n,end= " ")
        n+=1
    print()

# Row number triangle
for i in range(5):
    for j in range(0,i+1):
        print(i+1,end= " ")   
    print()

# 0-1 Triangle
for i in range(1,6):
    start = i%2
    for j in range(i):
        print(start,end = " ")
        start = 1-start
    print()
