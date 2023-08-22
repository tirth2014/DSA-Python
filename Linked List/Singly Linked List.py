"""
Singly Linked List

-------- Time Complexity ----------
Best Case:
Access	Search	Insertion  Deletion
 O(1)	 O(1)	 O(1)	     O(1)

Avg. Case:
Access	Search	Insertion  Deletion
  O(N)	 O(N)	  O(1)	    O(1)

Worst Case:
Access	Search	Insertion  Deletion
  O(N)	 O(N)	  O(N)	    O(N)
"""


from typing import Any

"""
Using property function of python for getter,setter methods

class Node:
    def __init__(self, data: Any):
        self._data = data
        self.next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data=None):
        self._data = data
"""


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        """
        This function is intended for iterators to access
        and iterate through data inside linked list.
        'in', 'enumerate' operators for LinkedList class object will work because of this function.
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __getitem__(self, index: int) -> Any:
        """
        Indexing Support. Used to get a node at particular position
        """
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")

        for i, node in enumerate(self):
            if i == index:
                return node
        return None

    def __len__(self) -> int:
        """
        Return length of linked list i.e. number of nodes
        """
        return sum(1 for _ in self)

    # Used to change the data of a particular node
    def __setitem__(self, index, data):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def insert_at_end(self, data: Any) -> None:
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.next = None

    def insert_at_start(self, data: Any):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_nth(self, index: int, data: Any):
        if not 0 <= index < len(self):
            raise IndexError("list index out of range")

        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def insert_after_node(self, prev_node, data: Any):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def is_data_present(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def delete_item(self,data):
        temp = self.head
        present = False
        if temp.data == data:
            self.head = temp.next
            return
        while temp and temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                present = True
            temp = temp.next
        if not present:
            raise ValueError(f'data {data} not present in linked list')

    def insert_after_data(self,prev_data,data):
        temp = self.head
        inserted = False
        while temp:
            if temp.data == prev_data:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                inserted = True
            temp = temp.next
        if not inserted:
            raise ValueError(f'data {prev_data} not present in linked list')


if __name__ == '__main__':
    ll = LinkedList()
    ll.head = Node(1)
    node2 = Node(2)
    ll.head.set_next(node2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_at_start(0)
    ll.insert_at_start(-1)
    ll.print_linked_list()
    ll.insert_at_nth(2, 5)
    print()
    print(ll[2])
    ll.print_linked_list()
    print('\n',ll.is_data_present(200))
    ll.insert_after_node(node2, 200)
    ll.print_linked_list()
    print('\n',ll.is_data_present(200))
    ll.delete_item(200)
    print()
    ll.print_linked_list()
    ll.delete_item(-1)
    print()
    ll.print_linked_list()
    ll.insert_after_data(5,50)
    ll.insert_at_start(5)
    ll.insert_at_nth(3, 5)
    ll.insert_after_data(5, 6)
    print()
    ll.print_linked_list()
    ll.delete_item(5)
    print()
    ll.print_linked_list()
    ll.insert_after_data(3,30)
    ll.insert_after_data(4,400)
    ll.insert_after_data(5,50)
    print()
    ll.print_linked_list()
    ll.insert_after_data(-1, 100)
    ll.delete_item(5)
