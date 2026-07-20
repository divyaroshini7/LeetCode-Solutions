class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        missing = len(t)
        left = start = end = 0

        for right, ch in enumerate(s, 1):
            if need.get(ch, 0) > 0:
                missing -= 1
            need[ch] = need.get(ch, 0) - 1

            if missing == 0:
                while left < right and need.get(s[left], 0) < 0:
                    need[s[left]] += 1
                    left += 1

                if end == 0 or right - left < end - start:
                    start, end = left, right

                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]