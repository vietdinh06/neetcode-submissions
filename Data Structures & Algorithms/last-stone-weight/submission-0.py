class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            stone_x = stones[len(stones)-1]
            stone_y = stones[len(stones)-2]

            if stone_x == stone_y:
                stones.pop()
                stones.pop()
            elif stone_x > stone_y:
                stones.pop()
                stones.pop()
                stones.append(stone_x - stone_y)

        if len(stones) == 1:
            return stones[0]

        else:
            return 0

            