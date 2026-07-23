class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        mx = max(freq.values())
        return max(len(tasks), (mx - 1) * (n + 1) + list(freq.values()).count(mx))   