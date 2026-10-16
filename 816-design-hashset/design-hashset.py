class node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.arr = [node(0) for i in range(10000)]

    def add(self, key: int) -> None:
        cur = self.arr[key % len(self.arr)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = node(key)

    def remove(self, key: int) -> None:
        cur = self.arr[key % len(self.arr)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.arr[key % len(self.arr)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False