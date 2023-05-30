# link: https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        self.map = {}
        

    def add(self, key: int) -> None:
        if key not in self.map:
            self.map[key] = 1
        

    def remove(self, key: int) -> None:
        if key in self.map:
            temp = self.map
            del temp[key]
            self.map = temp
        

    def contains(self, key: int) -> bool:
        if key in self.map:
            return True
        return False
