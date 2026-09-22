'''
381. Insert Delete GetRandom O(1) - Duplicates Allowed

RandomizedCollection is a data structure that contains a collection of numbers,
possibly duplicates.

Implement the RandomizedCollection class:

    RandomizedCollection()
        Initializes the empty collection.

    bool insert(int val)
        Inserts an item into the collection.
        Returns True if the collection did not already contain the element.

    bool remove(int val)
        Removes one occurrence of val from the collection if present.
        Returns True if an item was removed.

    int getRandom()
        Returns a random element from the current collection.
        The probability of each element being returned is proportional to the
        number of occurrences in the collection.

All operations must run in average O(1) time.

Example 1:
    Input:
        ["RandomizedCollection","insert","insert","insert",
         "getRandom","remove","getRandom"]

        [[],[1],[1],[2],[],[1],[]]

    Output:
        [null,true,false,true,1,true,1]

Explanation:
        Collection becomes [1,1,2].
        Removing one 1 leaves [1,2].
        getRandom returns 1 or 2 with equal probability.

Constraints:
    -2^31 <= val <= 2^31 - 1
    At most 2 * 10^5 calls will be made.
    There will always be at least one element when getRandom() is called.
'''

# HashMap + Dynamic Array Design

from collections import defaultdict
import random


class RandomizedCollection:

    def __init__(self):
        self.values = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        is_new = len(self.indices[val]) == 0

        self.values.append(val)
        self.indices[val].add(len(self.values) - 1)

        return is_new

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False

        remove_index = self.indices[val].pop()
        last_index = len(self.values) - 1
        last_value = self.values[last_index]

        if remove_index != last_index:
            self.values[remove_index] = last_value

            self.indices[last_value].remove(last_index)
            self.indices[last_value].add(remove_index)

        self.values.pop()

        if not self.indices[val]:
            del self.indices[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Example usage
randomizedCollection = RandomizedCollection()

print(randomizedCollection.insert(1))
# Output: True

print(randomizedCollection.insert(1))
# Output: False

print(randomizedCollection.insert(2))
# Output: True

print(randomizedCollection.getRandom())
# Output: 1 or 2 (1 has higher probability)

print(randomizedCollection.remove(1))
# Output: True

print(randomizedCollection.getRandom())
# Output: 1 or 2

print(randomizedCollection.insert(2))
# Output: False

print(randomizedCollection.remove(2))
# Output: True

print(randomizedCollection.getRandom())
# Output: 1 or 2
