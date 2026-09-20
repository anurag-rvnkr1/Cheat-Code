'''
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    - LRUCache(int capacity) initializes the cache with a positive size capacity.
    - int get(int key) returns the value of the key if the key exists, otherwise returns -1.
    - void put(int key, int value) updates the value of the key if the key exists.
      Otherwise, adds the key-value pair to the cache. If the number of keys exceeds
      the capacity, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
    Input:
        ["LRUCache","put","put","get","put","get","put","get","get","get"]
        [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

    Output:
        [null,null,null,1,null,-1,null,-1,3,4]

Explanation:
    LRUCache lRUCache = LRUCache(2);
    lRUCache.put(1,1);
    lRUCache.put(2,2);
    lRUCache.get(1);      // returns 1
    lRUCache.put(3,3);    // evicts key 2
    lRUCache.get(2);      // returns -1
    lRUCache.put(4,4);    // evicts key 1
    lRUCache.get(1);      // returns -1
    lRUCache.get(3);      // returns 3
    lRUCache.get(4);      // returns 4

Constraints:
    1 <= capacity <= 3000
    0 <= key <= 10^4
    0 <= value <= 10^5
    At most 2 * 10^5 calls will be made to get and put.
'''

# Doubly Linked List + HashMap


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node right after head (Most Recently Used)
    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move accessed node to front
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # Remove Least Recently Used node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]


# Example usage
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))  # Output: 1

cache.put(3, 3)      # Evicts key 2
print(cache.get(2))  # Output: -1

cache.put(4, 4)      # Evicts key 1
print(cache.get(1))  # Output: -1
print(cache.get(3))  # Output: 3
print(cache.get(4))  # Output: 4
