class RandomizedSet:

    def __init__(self):
        self.num_map = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        res = val not in self.num_map
        if res:
            idx = len(self.num_list)
            self.num_list.append(val)
            self.num_map[val] = idx
        return res

    def remove(self, val: int) -> bool:
        res = val in self.num_map
        if res:
            idx = self.num_map[val]
            moved = self.num_list[-1]
            self.num_list[idx] = moved
            self.num_list.pop()
            self.num_map[moved] = idx
            del self.num_map[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()