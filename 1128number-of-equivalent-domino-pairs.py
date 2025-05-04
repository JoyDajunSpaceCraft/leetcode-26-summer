
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = defaultdict(int)
        res = 0
        for (a, b) in dominoes:
            key = tuple(sorted((a, b)))
            print("key", key)
            res += count[key]
            count[key]+=1
        return res
        