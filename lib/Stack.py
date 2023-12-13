class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False        

    def push(self, item):
        if self.size() < self.limit:
           self.items.append(item)

    def pop(self):
       if len(self.items):
        return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
      # if self.size() <= self.limit:
      #   return True
      # else:
      #   return False
      return self.size() <= self.limit


    def search(self, target):
        for i, item in enumerate(self.items):
           if item == target:
              return len(self.items) - (i+1)
        return -1
