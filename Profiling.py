import cProfile
from Queue import Queue

def profile_queue(n):
    q = Queue()
    for i in range(n):
        q.enqueue(i)
    while not q.is_empty():
        q.dequeue()


def profile_list_as_queue(n):
    q = []
    for i in range(n):
        q.insert(0, 1)
    while len(q) > 0:
        q.pop()


def profile(n):
    profile_queue(n)
    profile_list_as_queue(n)


cProfile.run("profile(100000)")
