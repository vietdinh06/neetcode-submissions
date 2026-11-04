class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        best_k = 0

        while low <= high:
            k = (low + high) // 2

            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours > h:
                low = k + 1
            else:
                best_k = k
                high = k - 1

        return best_k