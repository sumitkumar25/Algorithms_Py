from bstNode import node


class BinarySearchTree:
    root = None

    def insert(self, root, item):
        if root:
            r = root
            while(r):
                if r.data >= item:
                    if r.left:
                        r = r.left
                    else:
                        r.left = node(item, None, None, r)
                        break

                elif r.data < item:
                    if r.right:
                        r = r.right
                    else:
                        r.right = node(item, None, None, r)
                        break
        else:
            self.root = node(item, None, None, None)

    def inOrderRecurse(self, root):
        if root:
            self.inOrderRecurse(root.left)
            print(root.data)
            self.inOrderRecurse(root.right)

    def preOrderRecurse(self, root):
        if root:
            print(root.data)
            self.inOrderRecurse(root.left)
            self.inOrderRecurse(root.right)

    def postOrderRecurse(self, root):
        if root:
            self.inOrderRecurse(root.left)
            self.inOrderRecurse(root.right)
            print(root.data)

    def inOrderIterate(self, root):
        r = root
        s = []
        while r or len(s):
            if r:
                s.append(r)
                r = r.left
            else:
                n = s.pop()
                print(n.data)
                r = n.right

    def preOrderIterate(self, root):
        s = [root]
        while len(s):
            n = s.pop()
            print(n.data)
            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.left)

    def postOrderIterate(self, root):
        r = root
        s = []
        while r or len(s):
            if r:
                s.append(r)
                r = r.left
            else:
                n = s.pop()
                print(n.data)
                r = n.right


t = BinarySearchTree()
t.insert(t.root, 10)
t.insert(t.root, 1)
t.insert(t.root, 110)
t.insert(t.root, 8)
t.insert(t.root, 4)
t.insert(t.root, 11)
t.insert(t.root, 7)
t.preOrderIterate(t.root)
t.preOrderRecurse(t.root)
