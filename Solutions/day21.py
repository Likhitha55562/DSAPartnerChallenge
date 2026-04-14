
# Day - 21 Solutions

# Combination Sum
def comb_sum(candidates,target):
    candidates.sort()
    res = []
    def backtrack(start,curr,rem):
        if rem == 0:
            res.append(curr[:])
            return
        for i in range(start,len(candidates)):
            if candidates[i]>rem:
                break
            curr.append(candidates[i])
            backtrack(i,curr,rem-candidates[i])
            curr.pop()
    backtrack(0,[],target)
    return res
print(comb_sum([2,3,6,7],7))

# Word Search 
def exist(board,word):
    rows,cols = len(board),len(board[0])
    def dfs(r,c,idx):
        if idx == len(word):
            return True
        if r<0 or r>=rows or c<0 or c>=cols:
            return False
        if board[r][c]!=word[idx]:
            return False
        temp = board[r][c]
        board[r][c] = '#'
        found = (
            dfs(r + 1, c, idx + 1) or
            dfs(r - 1, c, idx + 1) or
            dfs(r, c + 1, idx + 1) or
            dfs(r, c - 1, idx + 1)
        )
        board[r][c] = temp
        return found
    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    return False
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))

# Target Sum
def tar_sum(nums,target):
    def bt(idx,s):
        if idx==len(nums):
            return 1 if s==target else 0
        return bt(idx+1,s+nums[idx]) + bt(idx+1,s-nums[idx])
    return bt(0,0)
print(tar_sum([1,1,1,1,1],3))
    
    