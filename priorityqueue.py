import heapq
a=[3,100,99,5,6,9]
heapq.heapify(a)
a.remove(3)
heapq.heapify(a)
a.remove(5) #自個remove要再heapify
heapq.heapify(a)
print(a[0])
heapq.heappop(a)
print(a)
heapq.heappush(a,4)
print(a)
