class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)-1
        i = 0
        j = length
        volumes = []
        while i < j:
            volume = min([heights[i], heights[j]])*(j-i)
            volumes.append(volume)
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
        return max(volumes)
        