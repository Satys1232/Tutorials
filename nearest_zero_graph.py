from collections import deque
from copy import deepcopy
class Solution:
    # def nearest_zero(self , matrix , rows , cols , lst ,count = 1 , mincount = 0):
    #     for row in range(rows):
    #         for col in range(cols):
    #             if matrix[row][col] == 0:
    #                 lst[row][col] = 0
    #             else:
    #                 visited =  [[ 0 for _ in range(rows)] for _ in range(cols) ]
    #                 queue.append((row , col))
    #                 while len(queue) != 0:
    #                     queue.popleft()
    #                     for dx , dy in [(1, 0) , (-1 , 0) , (0 , 1) , (-1 , 0)]:
    #                         new_row = row + dx
    #                         new_col = col + dy
    #                         if new_row < 0 or new_row == rows or new_col < 0 or new_col == cols and  visited[new_row][new_col] == 0:
    #                             continue
    #                         if matrix[new_row][new_col] == 0:
    #                             lst[new_row][new_col] == count
    #                             break
    #                         else:
    #                             queue.append((new_row, new_col))
    #                             visited[new_row][new_col] = 1

    def updateMatrix(self , matrix):
        row = len(matrix)
        col = len(matrix[0])
        # for the reason visited and result need same number of 
        # rows and columns i created the row and col variable
        visited = [[0 for _ in range(col)] for _ in range(row)]
        distance =[[0 for _ in range(col)] for _ in range(row)]
        # it is sued to make rows and cols of the 
        queue = deque([])
        # since we are using bfs for it so we are using queue
        # to store the next value 
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    queue.append([i , j , 0])
                    visited[i][j] = 1
        """ We are doing like this means from 0 we are calculating distance
        in how much distance the 1 is and also the question name is 
         multi source bfs so we would be doing search from multiple 
         zeroes simultaneously and checking the ones and update it in result
        queue and we will put the location and distance [ ( i ,  j) , 0]
         as distance of 0 from 0 is zero we would put it zero """
        while len(queue) != 0:
    #     we are running till null because it will cover all the cells
    #     and update the value in the result list 
    #     we will be updating the distance for 1 only because 0s are 
    #     already visited so don't worry for that 
            i , j , d =   queue.popleft()
            distance[i][j] = d

        # i am updating distance here the reason is that 
        # why we have created the result list for keeping the result into
        # it right so when we do update when we have the distance and the 
        # moment we pop from the list , we get the row , col and distance 
        # so update it and also in the next iterations , it will get 
        # stored like row , col distance so until list is empty it will
        # get updated like this 
            for x , y in [(-1 , 0) , ( 0 , -1) ,( 0 , 1) , (1 , 0)]:
                new_i , new_j = i + x  , j + y
            # for going some where we need to create that where
            # we want to go so that we have ccreated here new cell
            # location
                if new_i < 0 or new_i == row or new_j < 0 or new_j == col:
                    continue
                if visited[new_i][new_j] == 1:
                    continue
                queue.append([new_i, new_j , d+1])
                visited[new_i][new_j] = 1
            # Here i have written d + 1 , it means that whenever i am 
            # going to a new cell it means it is 1 and it would be one
            # distance more than from the 0 so d + 1 , now why not 1 
            # directly , because when we are writing 1 we assume that 
            # there are no more cell with 1 , because we are visiting
            # one cell only and if there is another 1 it means it's 
            # distance from 0 is 2 so from this now d + 1 it would 
            # do another + 1 so 2 
        return distance





# --------------
# 1  |  1  |  1
# --------------
# 1  |  0  |  1
# --------------
# 0  |  1  |  0
# --------------

# 1. How to move and update distance using queue and run how many times 
# 2. How to find the distance and how the shortest is updated
# 3. How to maintain track of visited

# How we are able to store that row and column with distance 
sol = Solution()
matrix = [
    [1 , 1 , 1],
    [1 , 0 , 1],
    [0 , 1 , 0]
]
result = sol.updateMatrix(matrix)
print(*result)
