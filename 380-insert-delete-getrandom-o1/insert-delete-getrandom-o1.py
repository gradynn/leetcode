class RandomizedSet:

    def __init__(self):
        self.r_set = {}

    def insert(self, val: int) -> bool:
        try:
            self.r_set[val]
            return False
        except:
            self.r_set[val] = True
            return True

    def remove(self, val: int) -> bool:
        try:
            self.r_set[val]
            del self.r_set[val]
            return True
        except:
            return False

    def getRandom(self) -> int:
        rand = random.choice(list(self.r_set.keys()))
        return rand


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()