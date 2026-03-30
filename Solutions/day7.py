
# Day - 7 Solutions


# Smallest number
arr = [2,5,1,7,3,0]
min_val = arr[0]
for val in arr:
    if val<min_val[1:]:
        min_val = val
print(min_val)

# Largest number
arr = [2,5,1,7,3,0]
max_val = arr[0]
for val in arr[1:]:
    if val>max_val:
        max_val = val
print(max_val)

# Second smallest and largest
arr = [54,33,7,2,65,87]
arr.sort()
print(arr[1])
print(arr[-2])

# Reverse an array
arr = [4,2,1,64,13]
left = 0
right = len(arr)-1
while left<right:
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
print(arr)

# Count frequency of each element
arr = [1,1,3,6,2,1,6,8]
freq = {}
for val in arr:
   if val in freq:
      freq[val]+=1
   else:
      freq[val]=1
print(freq)

# Rearrange asc and desc order
arr = [1,2,3,4,5,6]
arr.sort()
half = len(arr)//2
arr = arr[:half] + arr[:half-1:-1]
print(arr)

# Sum of elements
arr = [2,5,34,641,2]
print(sum(arr))

# Average of all elements
arr = [4,2,5,1,5,6]
avg = sum(arr)/len(arr)
print(f"The average is : {avg:.2f}")

# Median of the array
arr = [3,4,1,5,6,5,9]
arr.sort()
length = int(len(arr))
if length%2!=0:
    print(arr[length//2])
else:
    print((arr[length//2-1]+arr[length//2])/2)
