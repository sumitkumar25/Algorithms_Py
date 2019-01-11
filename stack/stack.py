class Stack:
    def __init__(self):
        self._ = list()

    def push(self, a):
        self._.append(a)

    def pop(self):
        if(self.isEmpty()):
            print("Error Stack underflow")
            return
        return self._.pop()

    def isEmpty(self):
        return len(self._) == 0

