class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n) - linear time
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string = f"[{last.value}"
          
            while last.next:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"

            return return_string

    # O(n) - linear time
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) - linear time
    def __len__(self):
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    # O(1) - constant time
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            last_node = Node(value)
            last_node.previous = self.tail
            self.tail.next = last_node
            self.tail = last_node

    # O(1) - constant time
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first_node = Node(value)
            first_node.next = self.head
            self.head.previous = first_node
            self.head = first_node

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index Out of Bounds")
            else:
                last = self.head
                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("Index Out of Bounds")
                    last = last.next

                new_node = Node(value)
                new_node.next = last.next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node
                last.next = new_node

    # O(n) - linear time
    def delete(self, value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next

    # O(n) - linear time
    def pop(self, index):
        if self.head is None:
            raise ValueError("Index Out of Bounds")
        else:
            last = self.head
            for i in range(index-1):
                if last.next is None:
                    raise ValueError("Index Out of Bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index Out of Bounds")
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                last.next = last.next.next

    def get(self, index):
        if self.head is None:
            raise ValueError("Index Out of Bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("Index Out of Bounds")
                last = last.next
            return last.value
