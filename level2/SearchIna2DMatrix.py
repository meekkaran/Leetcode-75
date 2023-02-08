class Solution:
  #O(log(nm) time and O(nm)space
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix),len(matrix[0])
        start = 0
        end = row*col - 1
    
        while start <= end:
            
            mid = (start+end)//2
            if  matrix[mid//col][mid%col] == target:
                return True
            if matrix[mid//col][mid%col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
