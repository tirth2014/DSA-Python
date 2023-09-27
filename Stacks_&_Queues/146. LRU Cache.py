# Using HashMap + Doubly Linked List
# T.C : O(N)
# S.C : O(1)

import ast
class LRUCache:
    
    class Node:
        def __init__(self, key=None, val=None):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after_head(self, node):
        head = self.head
        node.next = head.next
        node.prev = head
        head.next.prev = node
        head.next = node

    def update_to_recent(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.insert_after_head(node)

    def del_lru(self):
        tail = self.tail
        lru = tail.prev
        lru.prev.next = tail
        tail.prev = lru.prev

    # O(1)
    def get(self, key) -> int:
        cache = self.cache
        if key in cache:
            self.update_to_recent(cache[key])
            return cache[key].val
        return -1

    # O(1)
    def put(self, key: int, value: int) -> None:
        cache = self.cache

        if key in cache:
            cache[key].val = value
            self.update_to_recent(cache[key])
            return

        elif len(cache) >= self.capacity:
            lru_key = self.tail.prev.key
            del cache[lru_key]
            self.del_lru()

        node = self.Node(key, value)
        cache[key] = node
        self.insert_after_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

queries = ast.literal_eval(input("list of queries to fire: "))
values = ast.literal_eval(input("queries values list: "))

for i, q in enumerate(queries):
    if q == "LRUCache":
        capacity = values[i][0]
        obj = LRUCache(capacity)
    elif q == "put":
        obj.put(key=values[i][0], value=values[i][1])
    else:
        print(obj.get(key=values[i][0]), end= ' ')




# Using in-built OrderedDict from python collections library:

from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    # O(1)
    def get(self, key: cache) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    # O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
