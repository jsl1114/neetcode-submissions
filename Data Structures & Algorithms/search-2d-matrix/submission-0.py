class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr = 0, len(matrix) - 1
        lc, rc = 0, len(matrix[0]) - 1

        while lr <= rr:
            m = lr + (rr - lr) // 2
            
            # right row, search within
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                while lc <= rc:
                    mm = lc + (rc - lc) // 2
                    if matrix[m][mm] == target:
                        return True
                    elif matrix[m][mm] < target:
                        lc = mm + 1
                    else:
                        rc = mm - 1
                
                return False
            
            elif target > matrix[m][-1]:
                lr = m + 1
            else:
                rr = m - 1
        
        return False
                