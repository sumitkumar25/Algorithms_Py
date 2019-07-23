class DsQueue:
    def __init__(self):
        self._ = list()

    def enqueue(self, a):
        self._.append(a)

    def dequeue(self):
        if(self.isEmpty()):
            print("Error Stack underflow")
            return
        return self._.pop(0)

    def isEmpty(self):
        return len(self._) == 0

    def printQ(self):
        print(self._)
