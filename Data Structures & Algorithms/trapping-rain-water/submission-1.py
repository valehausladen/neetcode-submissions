class Solution:
    def trap(self, height: List[int]) -> int:
        until_max = height.index(max(height))
        left = height[:until_max+1]
        right = height[until_max:]
        right.reverse()
        i = 0
        j = 0
        final_volume = 0
        volume = 0
        while j<len(left):
            if left[j]<left[i]:
                volume += (left[i]-left[j])
                j+=1
            else:
                i = j
                final_volume+=volume
                volume = 0
                j+=1
        i = 0
        j = 0
        volume = 0
        while j<len(right):
            if right[j]<right[i]:
                volume += (right[i]-right[j])
                j+=1
            else:
                i = j
                final_volume+=volume
                volume = 0
                j+=1
        return final_volume



        