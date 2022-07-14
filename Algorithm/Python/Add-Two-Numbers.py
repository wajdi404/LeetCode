# A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.

# Node class
class Node:
   
    # Function to initialize the node object
    # List Node
    def __init__( self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize 
                          # next as null
   
# Linked List class
class LinkedList:
     
    # Function to initialize the Linked 
    # List object
    def __init__( self): 
        self.head = None

        
def appendHead( l, data):
    temp = l.head
    l.head = Node(data)
    l.head.next = temp

        
def addTwoNumbers( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    l3 = LinkedList()
    l1curr = l1.head
    l2curr = l2.head
    aux = 0
    
    while True:
        if l1curr and l2curr:
            sum = l1curr.data + l2curr.data
            if sum > 9:
                appendHead( l3, sum - 10)
                aux = 1
            else:
                appendHead( l3, sum + aux)
                aux = 0
            l1curr = l1curr.next
            l2curr = l2curr.next
        elif l1curr:
            appendHead( l3, l1curr.data)
            l1curr = l1curr.next
        elif l2curr:
            appendHead(l3, l2curr.data)
            l2curr = l2curr.next
        else:
            break
    
    return l3    
        
if __name__=='__main__':
  # Start with the empty LinkedList 
  l1 = LinkedList()
  l1.head = Node(2)
  l1.head.next = Node(4)
  l1.head.next.next = Node(3)
  
  l2 = LinkedList()
  l2.head = Node(5)
  l2.head.next = Node(6)
  l2.head.next.next = Node(4)
  
  l3 = addTwoNumbers( l1, l2)

  curr = l3.head
  while curr:
    print(curr.data)
    curr = curr.next

  
  
