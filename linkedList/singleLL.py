from linkedList.singleLLNode import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        if(self.head):
            last = self.__getLastNode()
            last.next = Node(value, None)
            pass
        else:
            self.head = Node(value, None)
        self.size = self.size+1

    def printLinkedList(self):
        n = self.head
        while n:
            print(n.data)
            n = n.next

    def getSize(self):
        print("linked list size", self.size)
        return self.size

    # private utils

    def __getLastNode(self):
        it = self.head
        while it.next:
            it = it.next
        return it
