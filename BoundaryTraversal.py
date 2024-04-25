class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
 
def printPreOrder(root):
    if root == None:
        return
 
    print(root.data, end = " ")
    printPreOrder(root.left)
    printPreOrder(root.right)
 
def printInOrder(root):
    if root == None:
        return
 
 
    printInOrder(root.left)
    print(root.data, end = " ")
    printInOrder(root.right) 
 
def printPostOrder(root):
    if root == None:
        return
 
    printPostOrder(root.left)
    printPostOrder(root.right) 
    print(root.data, end = " ")
    


def collectLeftBoundary(root, result):
    while root != None:
        if root.left == None and root.right == None:
            break
 
        result.append(root.data)
 
        if root.left != None:
            root = root.left 
        else:
            root = root.right
 
def collectLeafNodes(root, result):
    if root == None:
        return 
    if root.left == None and root.right == None:
        result.append(root.data)
        return
 
    collectLeafNodes(root.left, result)
    collectLeafNodes(root.right, result)
 
def collectRightBoundaryInReverseDirection(root, result):
 
    temp = []
    while root != None:
        if root.left == None and root.right == None:
            break
 
        temp.append(root.data)
 
        if root.right != None:
            root = root.right 
        else:
            root = root.left
 
    temp = temp[::-1]
    for ele in temp:
        result.append(ele)
 
def printBoundaryTraversal(root):
    result = []
 
    result.append(root.data)
    collectLeftBoundary(root.left, result)
 
    collectLeafNodes(root, result)
 
    collectRightBoundaryInReverseDirection(root.right, result)
 
    print(*result)



        
root=TreeNode(11)

obj1=TreeNode(7)
obj2=TreeNode(15)
obj3=TreeNode(5)
obj4=TreeNode(9)
obj5=TreeNode(13)
obj6=TreeNode(20)
obj7=TreeNode(3)
obj8=TreeNode(8)
obj9=TreeNode(10)
obj10=TreeNode(12)
obj11=TreeNode(14)
obj12=TreeNode(18)
obj13=TreeNode(25)



root.left=obj1
root.right=obj2

obj1.left=obj3
obj1.right=obj4


obj2.left=obj5
obj2.right=obj6

obj3.left=obj7

obj4.left=obj8
obj4.right=obj9


obj5.left=obj10
obj5.right=obj11

obj6.left=obj12
obj6.right=obj13

printBoundaryTraversal(root) 
