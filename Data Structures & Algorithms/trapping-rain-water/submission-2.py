class Solution:
    def calc_vol_until_max(self, l: List[int]) -> int:
        i = 0
        volume = 0
        final_volume = 0
        for j in range(len(l)):
            if l[j] < l[i]:
                volume += l[i] - l[j]
            else:
                i = j
                final_volume += volume
                volume = 0
        return final_volume

    def trap(self, height: List[int]) -> int:
        until_max = height.index(max(height))
        left = height[:until_max + 1]
        right = height[until_max:][::-1]
        return self.calc_vol_until_max(left) + self.calc_vol_until_max(right)