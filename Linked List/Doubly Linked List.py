"""
Doubly Linked List

Advantages of Doubly Linked List over the singly linked list:
-> A DLL can be traversed in both forward and backward directions.
-> The delete operation in DLL is more efficient if a pointer to the node to be deleted is given.
-> We can quickly insert a new node before a given node.
-> In a singly linked list, to delete a node, a pointer to the previous
node is needed. To get this previous node, sometimes the list is traversed. In DLL, we can get the previous node
using the previous pointer.

Disadvantages of Doubly Linked List over the singly linked list:
-> Every node of DLL Requires extra space for a previous pointer. It is possible to implement DLL with a single pointer though.
-> All operations require an extra pointer previous to be maintained. For example, in insertion, we need to modify previous
pointers together with the next pointers.

Applications of Doubly Linked List:
-> It is used by web browsers for backward and forward navigation of web pages LRU (
Least Recently Used ) / MRU ( Most Recently Used ) Cache are constructed using Doubly Linked Lists.
-> Used by various applications to maintain undo and redo functionalities.
-> In Operating Systems, a doubly linked list is maintained by thread scheduler to keep track of processes
that are being executed at that time.
"""


class Node:
    def __init__(self, data=None,prev=None):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        return sum(1 for _ in self)

    def insert_at_start(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.prev = None
            return
        temp = self.head
        new_node.prev = None
        new_node.next = temp
        temp.prev = new_node
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        new_node.prev = curr
        new_node.next = None
        curr.next = new_node

    def insert_at_nth(self,ind,data):
        if ind == 0:
            self.insert_at_start(data)
        elif ind >= len(self):
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            prev_node = self.head
            for _ in range(0,ind-1):
                prev_node = prev_node.next

            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next = new_node

    def insert_after(self,prev_data,data):
        curr = self.head
        ind = 0
        inserted = False
        try:
            while curr.data:
                curr = curr.next
                ind += 1
                if curr.data == prev_data:
                    self.insert_at_nth(ind+1,data)
                    inserted = True
        except:
            if not inserted:
                print(f"Cannot insert {data} as Node with value {prev_data} is not present")

    def delete(self,data):
        curr = self.head
        if curr.data == data:
            curr.next.prev = None
            self.head = curr.next
            return

        try:
            while curr.data != data:
                if not curr.next:
                    raise ValueError(f'Data {data} is not present')
                curr = curr.next

        # If error comes print error and then continue with the rest of the code.
        except ValueError as e:
            print(e)
            return

        if not curr.next:
            curr.prev.next = curr.next
            return

        curr.next.prev = curr.prev
        curr.prev.next = curr.next

    def display(self):
        node = self.head
        while node:
            print(node.data,end='<->')
            node = node.next
        print('None')

        """
        # This will also work because we have defined __iter__() method
        for node in self:
            print(node.data,end="<->")
        print('None')
        """


if __name__ == '__main__':

    dll = DoublyLinkedList()
    dll.insert_at_start(5)
    dll.insert_at_start(3)
    dll.insert_at_end(6)
    dll.insert_at_end(8)
    dll.insert_at_end(9)
    dll.insert_at_end(7)
    dll.insert_at_end(4)
    dll.display()
    dll.delete(3)
    dll.delete(4)
    dll.display()
    dll.delete(8)
    dll.display()
    dll.delete(8)
    dll.insert_at_nth(9,9)
    dll.display()
    dll.insert_after(7,5)
    dll.display()
    dll.insert_after(4,100)
    dll.display()
