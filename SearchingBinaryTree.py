class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None  
 
 
def insertIntoBST(root, ele):
    if root == None:
        newBlock = TreeNode(ele)
        return newBlock 
 
    if root.data < ele:
        root.right = insertIntoBST(root.right, ele)
    else:
        root.left = insertIntoBST(root.left, ele)
    return root
 
def searchInBST(root,target):
    if root==None:
        return False
    elif root.data==target:
        return True
    elif root.data<target:
        return searchInBST(root.right,target)
    return searchInBST(root.left,target)


    
 
n=int(input())
nums =list(map(int,input().split()))
 

 
 
root = None 
for ele in nums:
    root = insertIntoBST(root, ele)
    
target=int(input())
if searchInBST(root,target)==True:
    print("Target element is found")
else:
    print("Target element is not found")
 
    
