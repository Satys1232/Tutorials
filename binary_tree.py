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
def preorder_traversal(head):
    if head == None:
        return
    print(head.data)
    preorder_traversal(head.left)
    preorder_traversal(head.right)

if __name__ == "__main__":
    preorder_traversal(head)


