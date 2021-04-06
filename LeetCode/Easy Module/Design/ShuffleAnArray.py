from random import randint
from copy import deepcopy


class Solution:

    def __init__(self, nums):
        self.num = deepcopy(nums)
        self.temp = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.num

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        rand = randint(0, len(self.temp) - 1)
        self.temp[0], self.temp[rand] = self.temp[rand], self.temp[0]
        return self.temp


obj = Solution([5, 6, 3, 2, 0, 4])
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())