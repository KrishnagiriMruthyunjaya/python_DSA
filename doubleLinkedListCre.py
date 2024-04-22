class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
def addATTail(head,ele):
    newnode=node(ele)
    
    if head==None:
        return newnode
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newnode
    newnode.prev=tail
    return head

def printLTR(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()
    
def printRTL(head):
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.prev 
    print()

    
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=addATTail(head,ele)
printLTR(head)
printRTL(head)
    
