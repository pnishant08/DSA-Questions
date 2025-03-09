class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        extended_colors = colors + colors[:k-1]
        alternating = 1
        count = 0

        for i in range(1, len(extended_colors)):
            if extended_colors[i] != extended_colors[i - 1]:
                alternating += 1
                if alternating >= k:
                    count += 1
            else:
                alternating = 1

        return count
