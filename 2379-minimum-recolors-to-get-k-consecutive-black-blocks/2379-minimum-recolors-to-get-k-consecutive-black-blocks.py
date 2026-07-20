class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = 0
        # Count white blocks in the first window
        for i in range(k):
            if blocks[i] == 'W':
                white += 1
        ans = white
        # Slide the window
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                white -= 1
            if blocks[i] == 'W':
                white += 1
            ans = min(ans, white)
        return ans