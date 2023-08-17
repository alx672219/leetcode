class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows   == 0: return []
        elif numRows == 1: return [[1]]
        
        triangle = [[1]]
        
        for i in range(1,numRows):
            row = [1] # each row의 first 1
            for j in range(1,i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j]) 
                          # 위 왼쪽                위 오른쪽
            row.append(1) # each row의 last 1
            triangle.append(row)
        return triangle