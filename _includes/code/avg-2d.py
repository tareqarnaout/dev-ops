def average_2D(matrix):
   N = len(matrix)        # number of rows
   M = len(matrix[0])     # number of columns (assumes at least one row)
   total = 0
   for r in range(N):
       for c in range(M):
           total += matrix[r][c]
   
   return total / (N * M)