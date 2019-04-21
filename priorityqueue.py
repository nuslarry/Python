import heapq
a=[3,100,99,5,6,9]
heapq.heapify(a)
a.remove(3)
heapq.heapify(a)
a.remove(5)
heapq.heapify(a)
print(a[0])
