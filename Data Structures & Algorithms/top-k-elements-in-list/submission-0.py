class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}

        for num in nums:
            if num in numbers:
                numbers[num] += 1
            else:
                numbers[num] = 1

        result = []

        for i in range(k):
            max_key = max(numbers, key=numbers.get)
            result.append(max_key)
            numbers.pop(max_key)

        return result
