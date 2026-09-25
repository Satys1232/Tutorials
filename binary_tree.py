# import math
# from collections import deque
# class Node:
#     def __init__(self , data):
#         self.data = data
#         self.left = None
#         self.right = None

# drinks = Node("Drinks")
# hot = Node("Hot")
# cold = Node("Cold")
# tea = Node("Tea")
# black_tea = Node("Black Tea")
# dargelling_black_tea = Node("Dargelling Black Tea")
# cofee = Node("Cofee")
# cola = Node("Cola")
# fanta = Node("Fanta")
# head = drinks

# hot.left = tea
# hot.right = cofee
# tea.left = black_tea
# black_tea.left = dargelling_black_tea
# cold.left = cola
# cold.right = fanta
# drinks.left = hot
# drinks.right = cold

# """
#               drinks
#             /        \
#            hot        cold
#         /  \         /  \
#        tea   cofee  cola  fanta
#       / 
#     black tea
#     /
#   dargelling black tea
# 
# 
# """
# def preorder_traversal(head):
#     if head == None:
#         return
#     preorder_traversal(head.left)
#     print(head.data)
#     preorder_traversal(head.right)

# def inorder_traversal(head):
#     if head == None:
#         return
#     inorder_traversal(head.left)
#     print(head.data)
#     inorder_traversal(head.right)

# def postorder_traversal(head):
#     if head == None:
#         return
#     postorder_traversal(head.left)
#     postorder_traversal(head.right)
#     print(head.data)

# def levelorder_traversal(head):
#     res = []
#     queue = deque([])
#     queue.append(head)
#     while len(queue) != 0:
#         e = queue.popleft()
#         res.append(e.data)
#         if e.left is not None:
#             queue.append(e.left)
#         if e.right is not None:
#             queue.append(e.right)
#     return res

# if __name__ == "__main__":
#     print(levelorder_traversal_with_height(head))

# def solve(head):
#     if head == None:
#         return 0
#     left_height = solve(head.left)
#     right_height = solve(head.right)
#     return 1 + max(left_height,right_height)

# def find_height(head):
#     queue = deque([])
#     height = 0
#     queue.append(head)
#     while len(queue) != 0:
#         level_size = len(queue)
#         height += 1
#         for _ in range(level_size):
#             e = queue.popleft()
#             if e.left is not None:
#                 queue.append(e.left)
#             if e.right is not None:
#                 queue.append(e.right)
#     return height
# print(find_height(head))
# class Solution:
#     def __init__(self):
#         self.diameter = 0
#     def solve(self, node):
#         if node is None:
#             return 0
#         left_height = self.solve(node.left)
#         right_height = self.solve(node.right)
#         self.diameter = max(self.diameter, left_height + right_height)
#         return 1 + max(left_height, right_height)
    # def diameterOfBinaryTree(self, root):
    #     self.diameter = 0
    #     self.solve(root)
    #     return self.diameter

# import math
# from collections import deque
# class Node:
#     def __init__(self , data):
#         self.data = data
#         self.left = None
#         self.right = None

# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# five = Node(5)
# six = Node(6)
# seven = Node(7)
# eight = Node(8)
# nine = Node(9)
# ten = Node(10)

# one.left = two
# one.right = three
# two.left = four
# two.right = five
# three.left = six
# three.right = seven
# four.left = eight
# eight.left = nine
# nine.left = ten

# head = one

# class Solution:
#     def solve(self, node):
#         if node is None:
#             return 0
#         left_height = self.solve(node.left)
#         right_height = self.solve(node.right)
#         if left_height is False or right_height is False:
#             return False
#         if abs(left_height - right_height) > 1:
#             return False
#         return 1 + max(left_height, right_height)

# sol = Solution()
# var = sol.solve(head)
# if var == False:
#     print("UnBalanced")
# if var != False:
#     print("Balanced")
# from collections import deque
# import math
# from collections import deque
# class Node:
#     def __init__(self , data):
#         self.data = data
#         self.left = None
#         self.right = None

# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# five = Node(5)
# six = Node(6)
# seven = Node(7)
# eight = Node(8)
# nine = Node(9)
# ten = Node(10)
# eleven = Node(11)


# one.left = two
# one.right = three
# two.left = four
# two.right = five
# three.left = six
# three.right = seven
# six.left = eight
# eight.left = nine
# nine.left = ten
# ten.left = eleven

# head = one

# import math
# class Solution:
#     def __init__(self):
#         self.maxie = -math.inf
#     def find_maxie(self, node):
#         if node is None:
#             return 0
#         left_gain = max(0, self.find_maxie(node.left))
#         right_gain = max(0, self.find_maxie(node.right))
#         current_path = left_gain + node.data + right_gain
#         self.maxie = max(self.maxie, current_path)
#         return node.data + max(left_gain, right_gain)
#     def return_maxie(self, node):
#         self.find_maxie(node)
#         return self.maxie

    #         5 
    #       /    \
    #     3       1
    #    /  \    /  \
    #   6    2  8    7


from collections import deque
import math
from collections import deque
class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

one = Node(5)
two = Node(3)
three = Node(1)
four = Node(6)
five = Node(2)
six = Node(8)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
eleven = Node(11)


one.left = two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven
# six.left = eight
# eight.left = nine
# nine.left = ten
# ten.left = eleven

head = one
# def topView(root):
#     if not root:
#         return None
#     ans = []
#     queue = deque()
#     result = {}
#     queue.append((root , 0))
#     while queue:
#         e , line = queue.popleft()
#         if line not in result:
#              result[line] = e.data
#         if e.left:
#             queue.append((e.left , line -1))
#         if e.right:
#             queue.append((e.right , line +1))
#     print(result)
#     for value in sorted(result.items()):
#         ans.append(value[1])
#     return ans

# print(topView(head))


# queue = deque()
# result = []
# queue.append(head)
# while len(queue) != 0:
#     level_size = len(queue)
#     for i in range(level_size):
#         node = queue.popleft()
#         if i == level_size - 1:
#             result.append(node.data)
#         if node.left :
#             queue.append(node.left)
#         if node.right :
#             queue.append(node.right)

# print(result)

def reverse_postorder(node , level , ans):
    if node is None:
        return
    if len(ans) == level:
        ans.append(node.data)
    if node.right:
        reverse_postorder(node.right , level + 1 , ans)
    if node.left:
        reverse_postorder(node.left , level + 1 , ans)
    return ans

print(reverse_postorder(head , 0 , []))
