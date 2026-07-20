class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        ans = []
        pc = [0] * 26
        wc = [0] * 26

        for ch in p:
            pc[ord(ch) - 97] += 1

        m = len(p)

        for i in range(len(s)):
            wc[ord(s[i]) - 97] += 1

            if i >= m:
                wc[ord(s[i - m]) - 97] -= 1

            if wc == pc:
                ans.append(i - m + 1)

        return ans