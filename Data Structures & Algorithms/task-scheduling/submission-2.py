import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        heap = []

        freq = {}

        for task in tasks:
            if task not in freq:
                freq[task] = 1
            else:
                freq[task] += 1

        for task in freq:
            heapq.heappush_max(heap, freq[task])

        time = 0
        q = deque() #count, time it become savil so cur time + n

        while heap or q:
            time += 1

            if heap:
                cnt = heapq.heappop_max(heap) - 1
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush_max(heap, q.popleft()[0])

        return time

        



    # trick is to always accomplish the task witht he largest number of frequencies, so when we wait fo r that character to open up, we can do another task
    # use a queue to denote at hat cycle doe sthe task become available
    # use heap to always select the character with largest frequenies first.
        
        

       