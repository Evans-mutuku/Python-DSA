import heapq

# Heap
heap = [43,14,1,88,8]

heapq.heapify(heap)
heapq.heappush(heap, 2)
print(heap)

# Stack
stack = []
stack.append(1)
stack.append(3)
stack.append(4)
stack.append(2)
print(stack.pop())