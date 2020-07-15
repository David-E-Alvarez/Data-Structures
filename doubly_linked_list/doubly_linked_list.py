"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        #checks to see if head
        if self.prev:
            self.prev.next = self.next
        #check to see if tail
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create node
        new_node = ListNode(value)
        self.length += 1
        #if list is empty set head and tail to new node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            print("head: ", self.head)
            print("tail: ", self.tail)

        else:
            #point current head's to node being made head which is current heads "prev"
            self.head.prev = new_node
            #print("self.head.prev: ", self.head.prev)
            #point node's next being added to current head
            new_node.next = self.head
            #print("new_node.next: ", new_node.next)
            #make new node the head
            self.head = new_node
            #print("self.head.value: ", self.head.value)
            #print("self.tail.value: ", self.tail.value)
    
            
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #create node
        new_node = ListNode(value)
        self.length += 1
        #if list is empty set head and tail to new node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #point tail's next to new node to create link
            self.tail.next = new_node
            #link new nodes "prev" to point to current tail
            new_node.prev = self.tail
            #make new node the tail
            self.tail = new_node
            # print("self.tail: ", self.tail.value)
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        #if list is empty
        if self.head is None and self.tail is None:
            print("nada")
            return 
        #if only one node
        if self.head is self.tail:
            self.head = None
            self.tail = None 
        #checks if either head or tail
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else: 
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = self.head.value
        #traverse and check if there is 


DLL = DoublyLinkedList()
print("DLL.__len__(): ", DLL.__len__())
DLL.add_to_head(1)
print("DLL.__len__(): ", DLL.__len__())
DLL.add_to_head(2)
print("DLL.__len__(): ", DLL.__len__())
DLL.add_to_tail(3)
print("DLL.__len__(): ", DLL.__len__())
DLL.remove_from_head()