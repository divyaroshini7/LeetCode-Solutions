class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []

        for ch in s:
            if ch.isalnum():
                temp.append(ch.lower())

        return temp == temp[::-1] 