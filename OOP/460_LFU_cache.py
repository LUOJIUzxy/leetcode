class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.user_counter = {}


    def get(self, key: int) -> int:
        if str(key) in self.cache:
            self.user_counter[str(key)] += 1
            return self.cache[str(key)]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        ## Add a new key
        if str(key) not in self.cache:
            ## remove the least frequently used key
            if len(self.cache) == self.capacity:
                min_counter = min(self.user_counter.values())
                
                for k, v in self.user_counter.items():
                    if v == min_counter:
                        self.cache.pop(k)
            self.cache[str(key)] = value
            self.user_counter[str(key)] = 1
            
        ## Uodate an existing key
        else:
            self.user_counter[str(key)] += 1
            self.cache[str(key)] = value


        


# Your LFUCache object will be instantiated and called as such:
capacity = 2
obj = LFUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)