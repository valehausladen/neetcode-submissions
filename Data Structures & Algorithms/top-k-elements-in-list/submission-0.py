class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for number in nums:
            if number not in numbers:
                numbers[number] = 1
            else:
                numbers[number] +=1
        return sorted(numbers, key=numbers.get, reverse=True)[:k]
