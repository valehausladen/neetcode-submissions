class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[:]
        suffix = nums[:]
        result = nums[:]
        n = len(nums)
        for i in range(n):
            if i == 0 or i == n-1:
                prefix[i] = nums[i]
                suffix[n-1] = nums[n-1]
            else:
                prefix[i] = prefix[i-1]*nums[i]
                suffix[n-i-1] = suffix[n-i+1-1]*nums[n-i-1]
        for j in range(n):
            if j == 0:
                result[j] = suffix[j+1]
            elif j == n-1:
                result[j] = prefix[j-1]
            else:
                result[j] = prefix[j-1]*suffix[j+1]
        return result
                
            

