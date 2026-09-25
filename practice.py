# from collections import deque
# queue = deque()
# rows = 0
# cols = 0
# while len(queue) != 0:
#     total_flooded = len(queue)
#     for _ in range(total_flooded):
#         i , j = queue.popleft()
#                     #        (-1 , 0) UP
#             #                  .
#             #                  .  
#             #  LEFT            .               RIGHT
#             # (0 , -1)  <----  * -----> (0 , 1)  
#             #                  .
#             #                  .
#             #                  .
#             #                (1 , 0) DOWN 
#         # Now i is 1 and j is 1
#         # So it would go to first right means : (0 ,1) -> (1 , 2)
#         # So new_i = 1 and new_j = 2
#         for dx , dy in [(0 , 1) , (0 , -1) , (-1 , 0) , (1 , 0)]:
#             new_i , new_j = i + dx , j + dy
#             if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
#                 continue


                       
                    
        