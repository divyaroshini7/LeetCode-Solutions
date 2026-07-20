class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        while n % 2 == 0:
            n //= 2
        ans = 1
        i = 3
        while i * i <= n:
            c = 1
            while n % i == 0:
                n //= i
                c += 1
            ans *= c
            i += 2
        return ans if n == 1 else ans * 2
        