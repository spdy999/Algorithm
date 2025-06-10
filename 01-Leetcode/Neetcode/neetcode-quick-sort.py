# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
from typing import List
from importlib.metadata import Pair


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        def qs(s: int, e: int):
            if e - s <= 0:
                return
            pivot = pairs[e]
            insertInd = s
            # Partition: elements smaller than pivot on left side
            for pt in range(s, e + 1):
                if pairs[pt].key < pivot.key:
                    pairs[insertInd], pairs[pt] = pairs[pt], pairs[insertInd]
                    insertInd += 1

            # Move pivot in-between left & right side
            pairs[insertInd], pairs[e] = pairs[e], pairs[insertInd]

            ls, le = s, insertInd - 1
            rs, re = insertInd + 1, e
            qs(ls, le)  # quick-sort left partition
            qs(rs, re)  # quick-sort right partition

        qs(0, n - 1)
        return pairs
