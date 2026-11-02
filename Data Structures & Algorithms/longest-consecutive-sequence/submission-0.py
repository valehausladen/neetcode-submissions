class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        length = len(nums)
        result = []
        cons = 1
        if length == 0:
            return 0 
        for i, sorted_num in enumerate(sorted_nums):
            if i != 0:
                if sorted_nums[i-1] == (sorted_num-1):
                    cons +=1
                elif sorted_nums[i-1] == sorted_num:
                    continue
                else:
                    result.append(cons)
                    cons = 1
        result.append(cons)
        return max(result)


            

        