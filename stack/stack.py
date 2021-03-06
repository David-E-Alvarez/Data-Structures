from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0 #for array
        #self.storage = []
        self.storage = LinkedList()

    def __len__(self): 
        return self.size


    def push(self, value):
        # self.storage.append(value)#for array
        self.size += 1 #for array
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size > 0: 
            self.size = self.size - 1
            return self.storage.remove_tail()
        



# stack_instance = Stack()
# stack_instance.push(1)
# print(stack_instance.__len__())
# stack_instance.push(2)
# print(stack_instance.__len__())
# stack_instance.push(2)
# stack_instance.push(3)
# stack_instance.push(4)
# print("size:",stack_instance.size)
# print('len: ',stack_instance.__len__())
# stack_instance.pop()
# print('len: ',stack_instance.__len__())
# print("size:",stack_instance.size)