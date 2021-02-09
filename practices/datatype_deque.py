from collections import deque


def deque_initialization():
    q = deque([1, 2, 3])
    assert len(q) == 3


def deque_operations():
    q = deque([1, 2, 3])

    q.append(4)
    assert q == deque([1, 2, 3, 4])

    k = q.popleft()
    assert k == 1
    assert q == deque([2, 3, 4])


if __name__ == '__main__':
    deque_initialization()
    deque_operations()
