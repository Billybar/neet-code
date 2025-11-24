import heapq # min heap is the default

nums = [5,7,9,1,3]

max_heap = []

for num in nums:
    heapq.heappush(max_heap, -num)

#peek
print(f"max: {-max_heap[0]}")\




