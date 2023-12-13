class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False        

    def push(self, item):
        self.items.append(item)

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        pass

    def full(self):
        pass

    def search(self, target):
        pass
