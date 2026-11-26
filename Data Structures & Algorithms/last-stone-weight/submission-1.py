import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone_x = heapq.heappop_max(stones)
            stone_y = heapq.heappop_max(stones)

            if stone_x == stone_y:
                continue

            if stone_x > stone_y:
                heapq.heappush_max(stones, stone_x - stone_y)

        return stones[0] if len(stones) == 1 else 0


        

            