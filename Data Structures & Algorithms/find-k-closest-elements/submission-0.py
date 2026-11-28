class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = []

        for num in arr:
            distances.append((abs(num - x), num))

        distances.sort()

        res = []

        for _, num in distances[:k]:
            res.append(num)

        return sorted(res)