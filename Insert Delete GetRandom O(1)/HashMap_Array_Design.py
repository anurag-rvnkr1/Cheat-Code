'''
380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:

    RandomizedSet()
        Initializes the object.

    bool insert(int val)
        Inserts val into the set if not present.
        Returns True if inserted, otherwise False.

    bool remove(int val)
        Removes val if present.
        Returns True if removed, otherwise False.

    int getRandom()
        Returns a random element from the current set.
        Every element must have the same probability of being returned.

All operations must work in average O(1) time.

Example 1:
    Input:
        ["RandomizedSet","insert","remove","insert",
         "getRandom","remove","insert","getRandom"]

        [[],[1],[2],[2],[],[1],[2],[]]

    Output:
        [null,true,false,true,2,true,false,2]

Constraints:
    -2^31 <= val <= 2^31 - 1
    At most 2 * 10^5 calls will be made.
    There will always be at least one element when getRandom() is called.
'''

# HashMap + Dynamic Array Design

import random


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False

        self.indices[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        remove_index = self.indices[val]
        last_value = self.values[-1]

        # Move last element into removed position.
        self.values[remove_index] = last_value
        self.indices[last_value] = remove_index

        # Remove last element.
        self.values.pop()
        del self.indices[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Example usage
randomizedSet = RandomizedSet()

print(randomizedSet.insert(1))
# Output: True

print(randomizedSet.remove(2))
# Output: False

print(randomizedSet.insert(2))
# Output: True

print(randomizedSet.getRandom())
# Output: 1 or 2

print(randomizedSet.remove(1))
# Output: True

print(randomizedSet.insert(2))
# Output: False

print(randomizedSet.getRandom())
# Output: 2

print(randomizedSet.insert(3))
# Output: True

print(randomizedSet.getRandom())
# Output: 2 or 3
