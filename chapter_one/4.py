# 找到最大或最小的n个元素
import heapq

nums = [1, 3, 5, 2, -1, 6, 4, 5, 4, 8, 9, 2, -2, -3, -4, -2, -3]

print(heapq.nlargest(4, nums))
print(heapq.nsmallest(4, nums))


heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heap[0])
