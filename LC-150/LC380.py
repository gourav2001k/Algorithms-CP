# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.list = []
        self.loc = dict()

    def insert(self, val: int) -> bool:
        if val in self.loc:
            return False
        self.loc[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.loc:
            return False
        idx = self.loc[val]
        n = len(self.list)
        self.list[idx] = self.list[n-1]
        self.loc[self.list[n-1]] = idx
        self.list.pop()
        del self.loc[val]
        return True

    def getRandom(self) -> int:
        n = len(self.list)
        idx = int(uniform(0, n))
        return self.list[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
