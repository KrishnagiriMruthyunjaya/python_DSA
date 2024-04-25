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

def fillInorder(inorder,root):
    if root==None:
        return
    fillInorder(inorder,root.left)
    inorder.append(root.data)
    fillInorder(inorder,root.right)

def findKthLargest(root,k):
    inorder=[]
    fillInorder(inorder,root)
    inorder=inorder[::-1]
    return inorder[k-1]
 
n=int(input())
nums =list(map(int,input().split()))
 

root = None 
for ele in nums:
    root = insertIntoBST(root, ele)

k=int(input())

print(findKthLargest(root,k))


