"""
Binary Indexed Tree

It is a data structure that supports sum range queries as well as setting values in a static array and
getting the value of the prefix sum up some index efficiently

"""
from typing import List


class FenwickTree:

    def __init__(self, values: List[int] = None):
        # contains fenwick tree ranges
        tree: List[int] = []

        if values:
            tree = values.copy()

            arr_len = len(values)
            for i in range(arr_len):
                j = i + self.lsb(i)
                if j < arr_len:
                    tree[j] += tree[i]

        self.tree = tree

    def lsb(self, value: int) -> int:
        """ Return least significant bit
        It just works magically, I don't know how!
        Maybe I know, for 2
        binary signed 2's complement of 2:  0000000000000010
                                                   &
        binary signed 2's complement of -2: 1111111111111110
                                          = 0000000000000010 = 2

        Args:
            value: Value to find its LSB

        Returns:
                LSB of the value
        """
        return value & -value

    def prefixSum(self, i: int) -> int:
        """ Computes prefix sum ftom [1,i] on based
        Args:
            i: Index for prefix sum from [1,i]

        Returns:
            Int
        """

        sum = 0
        while i != 0:
            sum += self.tree[i]
            # i &= ~self.lsb(i) # This is equals to i -=lsb(i). This is more readable but the first one is much faster
            i -= self.lsb(i)  # But we are using python, if you need that much optimization don't use python
        return sum

    def sum(self, i: int, j: int) -> int:
        """ Sum of the intervak [i,j], one based

        Args:
            i:
            j:

        Returns:

        """

        if j < i:
            raise ValueError('j cannot be smaller than i')

        return self.prefixSum(j) - self.prefixSum(i - 1)

    def add(self, i: int, k: int):

        while i < len(self.tree):
            self.tree[i] += k
            i += self.lsb(i)
