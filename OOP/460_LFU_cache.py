from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key : (value, freq)}
        self.user_counter = defaultdict(OrderedDict) # [ {key:value, key:value, key:value}, { ... }, {...} ]  
        #用空间换时间，直接每次记录当前最小的 min_freq
        self.min_freq = 0


    def get(self, key: int) -> int:
        if key in self.cache:
            value, freq = self.cache[key]
            # 从上一轮的freq里删除
            self.user_counter[freq].pop(key)
            # 从上一轮的freq+1里加入
            self.user_counter[freq + 1][key] = value
            self.cache[key] = (value, freq + 1)

            if not self.user_counter[freq]:
                del self.user_counter[freq]
                if self.min_freq == freq:
                    self.min_freq += 1

            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        ## Add a new key
        if key not in self.cache:
            ## remove the least frequently used key
            if len(self.cache) == self.capacity:
                # pop self.min_freq里最旧的那个
                remove, _ = self.user_counter[self.min_freq].popitem(last=False)
                self.cache.pop(remove)

        # freq = 1
            self.cache[key] = (value, 1)
            self.user_counter[1][key] = value
            self.min_freq = 1
            
        ## Update an existing key
        else:
            _, old_freq = self.cache[key]
            # 从上一轮的freq里删除
            self.user_counter[old_freq].pop(key)
            # 从上一轮的freq+1里加入
            self.user_counter[old_freq + 1][key] = value
            self.cache[key] = (value, old_freq + 1)

            if not self.user_counter[old_freq]:
                del self.user_counter[old_freq]
                if self.min_freq == old_freq:
                    self.min_freq += 1
        


# Your LFUCache object will be instantiated and called as such:
capacity = 2
obj = LFUCache(capacity)

args = [[1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
print(obj.put(args[0][0], args[0][1]))
print(obj.put(args[1][0], args[1][1]))
print(obj.get(args[2][0]))
print(obj.put(args[3][0], args[3][1]))
print(obj.get(args[4][0]))
print(obj.get(args[5][0]))
print(obj.put(args[6][0], args[6][1]))
print(obj.get(args[7][0]))
print(obj.get(args[8][0]))
print(obj.get(args[9][0]))
