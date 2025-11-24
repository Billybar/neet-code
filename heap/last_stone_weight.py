import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # build a data structure so we get the 2 heavyset stones
        # other words sort it fast as you can
        max_heap = [-num for num in stones]

        heapq.heapify(max_heap) # now we have max haep sorted in list

        while len(max_heap) > 1:
            # get top 2
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            new_stone = 0
            if y > x:
                new_stone = y-x
            heapq.heappush(max_heap, -new_stone)

        if len(max_heap) == 1:
            return -max_heap[0]
        return 0


