class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotate_top = 0
            rotate_buttom = 0

            for i in range(len(tops)):
                if tops[i]!=x and bottoms[i]!=x:
                    return -1
                elif tops[i]!=x:
                    rotate_top+=1
                elif bottoms[i]!=x:
                    rotate_buttom+=1
            return min(rotate_buttom, rotate_top)
        res = check(tops[0])
        if res != -1:
            return res
        else:
            res = check(bottoms[0])
            if res != -1:
                return res
            else:
                return -1