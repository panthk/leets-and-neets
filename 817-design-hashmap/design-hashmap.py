class Node:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.arr = [Node() for i in range(10**3)]

    def put(self, key: int, value: int) -> None:
        cur = self.arr[key % len(self.arr)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Node(key, value)


    def get(self, key: int) -> int:
        cur = self.arr[key % len(self.arr)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        cur = self.arr[key % len(self.arr)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next