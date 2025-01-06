class PriorityQueue:
    def __init__(self):
        self.arr = []
    
    def push(self, item):
        self.arr.append(item)
        self.arr.sort(reverse=True, key=lambda x: x[0]) # desc

    def pop(self):
        if self.isEmpty():
            return None
        return self.arr.pop()
    
    def isEmpty(self):
        return len(self.arr) == 0
