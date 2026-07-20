class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    for sub in dfs(end):
                        if sub == "":
                            result.append(word)
                        else:
                            result.append(word + " " + sub)

            memo[start] = result
            return result

        return dfs(0)