'''
170. Two Sum III - Data Structure Design

Design a data structure that accepts a stream of integers and checks whether
it has a pair of numbers whose sum equals a particular value.

Implement the TwoSum class:

    - TwoSum() initializes the TwoSum object.
    - void add(int number) adds number to the data structure.
    - bool find(int value) returns True if there exists any pair of numbers
      whose sum is equal to value, otherwise returns False.

Example 1:
    Input:
        ["TwoSum","add","add","add","find","find"]
        [[],[1],[3],[5],[4],[7]]

    Output:
        [null,null,null,null,true,false]

Explanation:
    TwoSum twoSum = new TwoSum();
    twoSum.add(1);
    twoSum.add(3);
    twoSum.add(5);
    twoSum.find(4); // True (1 + 3)
    twoSum.find(7); // False

Example 2:
    Input:
        ["TwoSum","add","add","find","find"]
        [[],[0],[0],[0],[1]]

    Output:
        [null,null,null,true,false]

Constraints:
    -10^5 <= number <= 10^5
    -2^31 <= value <= 2^31 - 1
    At most 5 * 10^4 calls will be made to add and find.
'''

# HashMap


class TwoSum:

    def __init__(self):
        self.numbers = {}

    def add(self, number: int) -> None:
        self.numbers[number] = self.numbers.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for num in self.numbers:
            complement = value - num

            if complement == num:
                if self.numbers[num] > 1:
                    return True
            elif complement in self.numbers:
                return True

        return False


# Example usage
twoSum = TwoSum()

# Example 1
twoSum.add(1)
twoSum.add(3)
twoSum.add(5)

print(twoSum.find(4))  # Output: True
print(twoSum.find(7))  # Output: False

# Example 2
twoSum2 = TwoSum()

twoSum2.add(0)
twoSum2.add(0)

print(twoSum2.find(0))  # Output: True
print(twoSum2.find(1))  # Output: False

# Example 3
twoSum3 = TwoSum()

twoSum3.add(2)
twoSum3.add(7)
twoSum3.add(11)
twoSum3.add(15)

print(twoSum3.find(9))   # Output: True
print(twoSum3.find(26))  # Output: True
print(twoSum3.find(20))  # Output: False
