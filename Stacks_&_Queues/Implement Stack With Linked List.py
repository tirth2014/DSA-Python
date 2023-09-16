class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Stack:
    # Write your code here
    def __init__(self):
        # Write your code here
        self.head = Node(None)

    def getSize(self):
        # Write your code here
        if not self.head:
            return 0
        temp = self.head
        size = 0
        while temp:
            temp = temp.next
            size += 1
        return size

    def isEmpty(self):
        # Write your code here
        if not head:
            return True
        return False

    def push(self, data):
        # Write your code here
        new = Node(data)
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        temp.next = new

    def pop(self):
        # Write your code here
        if self.head:
            if not self.head.next:
                self.head = None
            else:
                prev, temp = None, self.head
                while temp and temp.next:
                    prev = temp
                    temp = temp.next
                prev.next = None

    def getTop(self):
        if not self.head: return -1
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        return temp.data