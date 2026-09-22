'''
460. LFU Cache

Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

    LFUCache(capacity)
        Initializes the object with the cache capacity.

    get(key)
        Returns the value if the key exists; otherwise returns -1.

    put(key, value)
        Inserts or updates the value.
        If the cache reaches capacity, remove the least frequently used item.
        If multiple keys have the same frequency, remove the least recently used one.

All operations must run in O(1) average time.

Example 1:
    Input:
        ["LFUCache","put","put","get","put","get","get","put",
         "get","get","get"]

        [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

    Output:
        [null,null,null,1,null,-1,3,null,-1,3,4]

Constraints:
    0 <= capacity <= 10^4
    0 <= key <= 10^5
    0 <= value <= 10^9
    At most 2 * 10^5 calls will be made.
'''

# Design + HashMap + Doubly Linked List

from collections import defaultdict


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current_size = 0

        self.minimum_frequency = 0

        self.nodes = {}                       # key -> Node
        self.frequency_lists = defaultdict(DoublyLinkedList)

    def _update_frequency(self, node):
        frequency = node.freq

        self.frequency_lists[frequency].remove(node)

        if (
            frequency == self.minimum_frequency and
            self.frequency_lists[frequency].size == 0
        ):
            self.minimum_frequency += 1

        node.freq += 1
        self.frequency_lists[node.freq].insert_front(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self._update_frequency(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._update_frequency(node)
            return

        if self.current_size == self.capacity:
            node_to_remove = self.frequency_lists[
                self.minimum_frequency
            ].remove_last()

            del self.nodes[node_to_remove.key]
            self.current_size -= 1

        new_node = Node(key, value)

        self.nodes[key] = new_node
        self.frequency_lists[1].insert_front(new_node)

        self.minimum_frequency = 1
        self.current_size += 1


# Example usage

lfu = LFUCache(2)

lfu.put(1, 1)
lfu.put(2, 2)

print(lfu.get(1))
# Output: 1

lfu.put(3, 3)

print(lfu.get(2))
# Output: -1

print(lfu.get(3))
# Output: 3

lfu.put(4, 4)

print(lfu.get(1))
# Output: -1

print(lfu.get(3))
# Output: 3

print(lfu.get(4))
# Output: 4


# Example 2
lfu2 = LFUCache(1)

lfu2.put(1, 10)
print(lfu2.get(1))
# Output: 10

lfu2.put(2, 20)
print(lfu2.get(1))
# Output: -1

print(lfu2.get(2))
# Output: 20


# Example 3
lfu3 = LFUCache(0)

lfu3.put(1, 100)
print(lfu3.get(1))
# Output: -1


# Example 4
lfu4 = LFUCache(3)

lfu4.put(1, 1)
lfu4.put(2, 2)
lfu4.put(3, 3)

lfu4.get(1)
lfu4.get(1)
lfu4.get(2)

lfu4.put(4, 4)

print(lfu4.get(3))
# Output: -1

print(lfu4.get(1))
# Output: 1

print(lfu4.get(4))
# Output: 4


# Example 5
lfu5 = LFUCache(2)

lfu5.put(1, 10)
lfu5.put(2, 20)

lfu5.put(2, 200)

print(lfu5.get(2))
# Output: 200


# Example 6
lfu6 = LFUCache(2)

lfu6.put(5, 50)
lfu6.put(6, 60)

lfu6.get(5)
lfu6.get(6)
lfu6.get(6)

lfu6.put(7, 70)

print(lfu6.get(5))
# Output: -1

print(lfu6.get(6))
# Output: 60

print(lfu6.get(7))
# Output: 70
