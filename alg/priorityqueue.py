from queue import PriorityQueue
"""
优先队列
https://www.linode.com/docs/guides/python-priority-queue/
"""
a = PriorityQueue()
a.put(1)
a.put(2)
a.put(3)
a.put(4)
a.put(5)
while not a.empty():
    print('size: %d' % a.qsize())
    print('queue: %s' % a.get())
print(a.empty())
