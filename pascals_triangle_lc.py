class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle=[]
        for i in range(numRows):
            row=[0 for j in range(i+1)]
            row[0]=1
            row[-1]=1
            for k in range(1,len(row)-1):
                row[k]=triangle[i-1][k-1]+triangle[i-1][k]
            triangle.append(row)
        return triangle
