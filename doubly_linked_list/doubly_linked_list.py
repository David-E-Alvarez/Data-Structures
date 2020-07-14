"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_prev(self):
        return self.prev
    
    def set_prev(self, new_prev):
        self.prev = new_prev

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
            
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
        #1.)create Node from value being passed in
        new_node = ListNode(value)
        self.length += 1
        #check my list to see if empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #2.) make link
            self.head.set_next(new_node)
            #3.)move tail
            self.tail = new_node
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #1.)add node
        new_node = ListNode(value)
        self.length += 1
        #check to see if LL is empty and if so set "new_node" to both head/tail
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #2.)make link
            self.tail.set_next(new_node)
            #3.)move tail
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
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
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

DLL = DoublyLinkedList()
DLL.add_to_tail(1)
DLL.add_to_head(2)
print("DLL: ", DLL.__len__())
