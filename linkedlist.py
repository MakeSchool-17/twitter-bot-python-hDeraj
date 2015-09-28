class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        new_node = LinkedListNode(item)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find(self, condition_func):
        current = self.head
        while current:
            if condition_func(current.data):
                return current.data
        return None

    def delete(self, item):
        if not self.head:
            return
        if self.head.data == item:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        else:
            current = self.head
            while current.next:
                if current.next.data == item:
                    if not current.next.next:
                        # current.next is tail
                        current.next = None
                        self.tail = current
                    else:
                        current.next = current.next.next


class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
