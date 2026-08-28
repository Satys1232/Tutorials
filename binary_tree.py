class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

drinks = Node("Drinks")
hot = Node("Hot")
cold = Node("Cold")
tea = Node("Tea")
cofee = Node("Cofee")
cola = Node("Cola")
fanta = Node("Fanta")
head = drinks

hot.left = tea
hot.right = cofee
cold.left = cola
cold.right = fanta
drinks.left = hot
drinks.right = cold

# """
#               drinks
#             /        \
#            hot        cold
#         /  \         /  \
#        tea   cofee  cola  fanta
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

def postorder_traversal(head):
    if head == None:
        return
    postorder_traversal(head.left)
    postorder_traversal(head.right)
    print(head.data)


if __name__ == "__main__":
    postorder_traversal(head)


