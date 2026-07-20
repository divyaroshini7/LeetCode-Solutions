class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n > 1 and n not in s:
            s.add(n)
            n = sum(int(x) * int(x) for x in str(n))
        return n == 1 