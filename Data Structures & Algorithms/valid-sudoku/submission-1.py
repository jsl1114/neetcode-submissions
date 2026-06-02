class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                curEle = board[i][j]
                if curEle == '.':
                    continue
                if curEle in rows[i] or curEle in cols[j] or curEle in squares[(i // 3, j // 3)]:
                    return False
                rows[i].add(curEle)
                cols[j].add(curEle)
                squares[(i // 3, j // 3)].add(curEle)
        
        return True
