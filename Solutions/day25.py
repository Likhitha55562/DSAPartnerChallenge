
# Day - 25 solutions

# Sudoku Solver
def sudsolver(board):
    def is_valid(r,c,ch):
        for i in range(9):
            if board[r][i]==ch or board[i][c]==ch:
                return False
            if board[3*(r//3)+i//3][3*(c//3)+i%3] == ch:
                return False
        return True
    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    for ch in '123456789':
                        if is_valid(r,c,ch):
                            board[r][c] = ch
                            if solve():
                               return True
                            board[r][c] = '.'
                    return False
        return True
    solve()
    return board
print(sudsolver([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
                 ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
                 [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))



# Letter Tile Possibilities 
def numTilesPossibilites(tiles):
    freq = [0]*26
    for c in tiles:
        freq[ord(c)-ord('A')]+=1
        def  count():
            res = 0
            for i in range(26):
                if freq[i]>0:
                    res+=1
                    freq[i]-=1
                    res+=count()
                    freq[i]+=1
            return res
    return count()
print(numTilesPossibilites("AAB"))

# All Paths From Source to Target
def all_paths(graph):
    res = []
    def dfs(node,path):
        if node==len(graph)-1:
            res.append(path[:])
            return
        for nx in graph[node]:
            path.append(nx)
            dfs(nx,path)
            path.pop()
    dfs(0,[0])
    return res
print(all_paths([[1,2],[3],[3],[]]))