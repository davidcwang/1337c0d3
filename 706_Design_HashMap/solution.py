"""
Problem: 706. Design HashMap
Url: https://leetcode.com/problems/design-hashmap/
Author: David Wang
Date: 05/28/2020
"""

SIZE = 100000

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = [[] for i in range(SIZE)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash = key % SIZE
        bucket = self.array[hash]

        if len(bucket) > 0:
            for i, entry in enumerate(bucket):
                if entry.key == key:
                    bucket[i].value = value
                    break

        else:
            bucket.append(Entry(key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash = key % SIZE
        bucket = self.array[hash]

        for entry in bucket:
            if entry.key == key:
                return entry.value

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash = key % SIZE
        bucket = self.array[hash]

        for i, entry in enumerate(bucket):
            if entry.key == key:
                bucket.pop(i)
                return


if __name__ == '__main__':
    # Your MyHashMap object will be instantiated and called as such:
    key = 1
    value = 2
    obj = MyHashMap()
    obj.put(key,value)
    value1 = obj.get(key)
    obj.remove(key)
    value2 = obj.get(key)

    assert value1 == 2
    assert value2 == -1


