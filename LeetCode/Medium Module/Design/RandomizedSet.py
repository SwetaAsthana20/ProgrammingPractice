import random
from math import floor


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_list = []
        self.num_map = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_map:
            return False

        self.num_list.append(val)
        self.num_map[val] = len(self.num_list) - 1

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.num_map:
            return False

        rm_index = self.num_map[val]
        self.num_list[rm_index] = self.num_list[-1]
        self.num_map[self.num_list[-1]] = rm_index
        del self.num_map[val]
        self.num_list.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        random_index = floor(random.random() * len(self.num_list))
        return self.num_list[random_index]


obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(10))
print(obj.insert(30))
print(obj.insert(50))
print(obj.insert(70))
print(obj.remove(2))
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
print(obj.getRandom())
