from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.stack = deque()

    def get(self, key: int) -> int:
        if str(key) in self.cache:
            self.stack.remove(str(key))
            self.stack.append(str(key))
            return self.cache[str(key)]
        else: 
            return -1 
        

    def put(self, key: int, value: int) -> None:
        ## Add a new key
        if str(key) not in self.cache:
            
            if len(self.cache.keys()) == self.capacity:
                # recently updated key
                lru_key = self.stack.popleft()
                self.cache.pop(lru_key)
            self.stack.append(str(key))

            self.cache[str(key)] = value
        else:
            # update an existed key
            self.cache[str(key)] = value
            self.stack.remove(str(key))
            self.stack.append(str(key))

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)