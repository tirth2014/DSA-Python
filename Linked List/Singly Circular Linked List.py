"""
Singly Circular Linked List
https://www.geeksforgeeks.org/circular-linked-list/
"""


class Node:
    def __init__(self, data=None,prev=None):
        self.data = data
        self.next = None


class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        new_node = Node(data)
        curr = self.head
        old_head = self.head
        if not curr:
            self.head = new_node
            new_node.next = new_node
            return

        new_node.next = curr
        while curr.next != old_head:
            curr = curr.next
        curr.next = new_node
        self.head = new_node

    def insert_at_end(self,data):
        curr = self.head
        if not curr:
            self.insert_at_start(data)
            return

        new_node = Node(data)
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def delete(self,data):
        temp = prev = self.head
        if not temp:
            print("List is empty!")
            return

        if temp.data == data:
            if temp.next == temp:
                self.head = None
            else:
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = temp.next
            return

        temp = temp.next
        if temp == self.head:
            return
        while temp != self.head:
            prev = temp
            temp = temp.next
            if temp.data == data:
                prev.next = temp.next

    def display(self):
        node = self.head
        if not node:
            print("List is empty!")
            return

        print('->',node.data,end='->')
        node = node.next
        while node != self.head:
            print(node.data, end="->")
            node = node.next
        print()


if __name__ == '__main__':

    cll = SinglyCircularLinkedList()
    cll.insert_at_start(2)
    cll.insert_at_start(1)
    cll.insert_at_start(3)
    cll.display()  # -> 3->1->2->
    cll.insert_at_end(8)
    cll.insert_at_end(10)
    cll.display()
    cll.delete(3)
    cll.display()
    cll.delete(8)
    cll.display()
    cll.delete(10)
    cll.display()
