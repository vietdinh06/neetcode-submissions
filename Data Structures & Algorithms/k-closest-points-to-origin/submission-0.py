import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        mapped_distances = {}
        origin = [0, 0]
        result = []

        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if distance not in mapped_distances:
                mapped_distances[distance] = []

            mapped_distances[distance].append(point)

            heapq.heappush_max(heap, distance)

            if len(heap) > k:
                heapq.heappop_max(heap)

        for distance in heap:
            point = mapped_distances[distance].pop()
            result.append(point)

        return result




        
            