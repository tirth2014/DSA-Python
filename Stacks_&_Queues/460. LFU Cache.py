# Two dict + Doubly linked list
# https://leetcode.com/problems/lfu-cache
# Explanation: https://leetcode.com/problems/lfu-cache/solutions/207673/python-concise-solution-detailed-explanation-two-dict-doubly-linked-list/


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

import ast

class Node:
    def __init__(self, key=None, val=None, freq=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.size = 0
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after_head(self, node):
        self.size += 1
        head = self.head
        node.next = head.next
        node.prev = head
        head.next.prev = node
        head.next = node

    def pop_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def del_lfu_lru(self):
        tail = self.tail
        lru = tail.prev
        lru.prev.next = tail
        tail.prev = lru.prev
        self.size -= 1

class LFUCache:

    def __init__(self, capacity: int):
        self.min_freq = 0
        self.cache = {}  # maps key,node
        self.freq_map = {}  # maps freq,DLL
        self.freq_map[1] = DLL()
        self.capacity = capacity

    def update_to_recent(self,node):
        freq = node.freq
        self.freq_map[freq].pop_node(node)
        node.freq += 1

        new_freq = node.freq
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = DLL()
        self.freq_map[new_freq].insert_after_head(node)
        if self.freq_map[self.min_freq].size == 0:
            self.min_freq += 1
        return node.val

    # O(1)
    def get(self, key) -> int:
        cache = self.cache
        if key in cache:
            node = cache[key]
            self.update_to_recent(node)
            return node.val
        return -1

    # O(1)
    def put(self, key: int, value: int) -> None:
        cache = self.cache

        if self.capacity == 0:
            return

        if key in cache:
            node = cache[key]
            self.update_to_recent(node)
            node.val = value

        else:
            if len(cache) >= self.capacity:
                lfu_lru_key = self.freq_map[self.min_freq].tail.prev.key
                del cache[lfu_lru_key]
                self.freq_map[self.min_freq].del_lfu_lru()

            self.min_freq = 1
            node = Node(key,value,1)
            cache[key] = node
            self.freq_map[self.min_freq].insert_after_head(node)



# queries = ast.literal_eval(input("list of queries to fire: "))
# values = ast.literal_eval(input("queries values list: "))
queries = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
values = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output: [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

for i, q in enumerate(queries):
    if q == "LFUCache":
        capacity = values[i][0]
        obj = LFUCache(capacity)
    elif q == "put":
        obj.put(key=values[i][0], value=values[i][1])
    else:
        print(obj.get(key=values[i][0]), end=' ')
