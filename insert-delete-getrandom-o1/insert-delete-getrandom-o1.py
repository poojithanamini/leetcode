class RandomizedSet:

    def __init__(self):
        self.mylist = []
        self.mydict = {}
        self.length = -1
    def insert(self, val: int) -> bool:
        if val in self.mydict:
            return False
        self.mylist.append(val)
        self.length += 1
        self.mydict[val] = self.length
        return True
    def remove(self, val: int) -> bool:
        if val not in self.mydict:
            return False
        index_to_remove = self.mydict[val]
        self.mylist[index_to_remove] = self.mylist[-1]
        self.mydict[self.mylist[index_to_remove]] = index_to_remove
        self.mylist.pop()
        self.mydict.pop(val)
        self.length -= 1
        return True
    def getRandom(self) -> int:
        return self.mylist[random.randrange(self.length + 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()