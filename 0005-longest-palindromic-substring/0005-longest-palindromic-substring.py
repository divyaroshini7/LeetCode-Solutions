class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    ans = max(ans, s[l:r + 1], key=len)
                    l -= 1
                    r += 1
        return ans
