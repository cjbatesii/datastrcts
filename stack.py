class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
     def __init__(self):
         self.top = None
         self.size = 0

     # O(1) - constant time
     def __len__(self):
         return self.size

     # O(1) - constant time
     def __repr__(self):
         items = []
         current_item = self.top
         while current_item is not None:
             items.append(str(current_item.value))
             current_item = current_item.next
         return "["+', '.join(items)+"]"

     # O(1) - constant time
     def push(self, value):
         new_node = Node(value)
         new_node.next = self.top
         self.top = new_node
         self.size += 1

     # O(1) - constant time
     def pop(self):
         if self.top is None:
             raise ValueError("Stack is Empty")
         pop_value = self.top.value
         self.top = self.top.next
         self.size -= 1

         return pop_value

     # O(1) - constant time
     def peek(self):
         if self.top is None:
             raise ValueError("Stack is Empty")
         return self.top.value

     # O(1) - constant time
     def is_empty(self):
         return self.top is None
