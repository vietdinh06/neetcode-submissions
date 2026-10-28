class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1


        while a < b:
            pair = numbers[a] + numbers[b]

            if pair == target:
                break

            if pair < target:
                a += 1

            if pair > target:
                b -= 1


        return [a+1, b+1]
        