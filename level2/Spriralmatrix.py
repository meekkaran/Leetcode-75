class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        #have 4 pointers on diffent positions in the matrix
        left = 0;
        top = 0;
        right=len(matrix[0])
        bottom=len(matrix)#no. of rows
        #we are moving to the right, then down, then to the left, and finally moving up.
        #remember to update pointers when moving from one direction to another
        
        while left < right and top < bottom:
            #get every i in the top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1#shift top pointer down by 1
            
            #get every i in the right column
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right -=1#shift the right pointer to the left
            
            if not (left < right and top < bottom):
                break
            
            #get every i in the bottom row
            for i in range (right-1,left-1,-1):#we are adding -1 since we are doing this in reverse order(right to left)
                res.append(matrix[bottom-1][i])     
            bottom -= 1
            
            #get every i in the left collumn
            for i in range(bottom-1,top-1,-1):#we are adding -1 since we are doing this in reverse order(bottom to top)
                res.append(matrix[i][left])
            left += 1#shift left pointer to the right
        return res
            
                
        
        
