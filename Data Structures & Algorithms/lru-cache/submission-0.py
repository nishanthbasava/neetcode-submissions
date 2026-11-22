class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    # Both put and get have time complexity of O(1), space complexity is O(capacity)
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node() # dummy node on the least recent side
        self.tail = Node() # dummy node on the most recent side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_end(self, node: Node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def _usage(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self._add_to_end(node)

    def _remove(self):
        self.cache.pop(self.head.next.key)
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        

    def get(self, key: int):
        if key in self.cache:
            self._usage(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int): 
        if key in self.cache:
            self._usage(self.cache[key])
            self.cache[key].value = value
        else:
            if len(self.cache) >= self.capacity:
                self._remove()
            self.cache[key] = Node(key, value)
            self._add_to_end(self.cache[key])