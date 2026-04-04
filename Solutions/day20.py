
# Day - 20 Solutions

# Number of Steps to Reduce a Number to Zero
def num_of_steps(n):
    if n==0:
        return 0
    return 1+ num_of_steps(n>>1 if n%2==0 else n-1)
print(num_of_steps(14))

# Check Balanced Parentheses using Recursion (no stack)
def is_balanced(s,idx=0,balance=0):
    if balance<0:
        return False
    if idx==len(s):
        return balance==0
    if s[idx] == '(':
        return is_balanced(s,idx+1,balance+1)
    if s[idx] == ')':
        return is_balanced(s,idx+1,balance-1)
    return is_balanced(s,idx+1,balance)
print(is_balanced("()("))

# Remove Consecutive Duplicate Characters
def remove_dupli(s):
    if len(s)<=1:
        return s
    if s[0]==s[1]:
        return remove_dupli(s[1:])
    return s[0] + remove_dupli(s[1:])
print(remove_dupli("aabba"))

# Print All Palindromic Partitions 
def palindromic_partion(s,start=0,cur=[],res=[]):
    if start == len(s):
        res.append(cur[:])
        return
    for end in range(start+1,len(s)+1):
        prefix = s[start:end]
        if prefix == prefix[::-1]:
            cur.append(prefix)
            palindromic_partion(s,end,cur,res)
            cur.pop()
    return  res
print(palindromic_partion("aab"))


# Power Set / All Permutations in Lexicographic Order 
def power_sets(s,idx=0,current = '',res=[]):
    if res is None:
        res = []
    if idx==len(s):
        res.append(current)
        return res
    power_sets(s,idx+1,current+s[idx],res)
    power_sets(s,idx+1,current,res)
    return res
print(power_sets("ab"))
from itertools import permutations
s = "ab"
sorted([''.join(p) for p in permutations(sorted(s))])