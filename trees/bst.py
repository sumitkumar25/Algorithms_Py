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
            self.preOrderRecurse(root.left)
            self.preOrderRecurse(root.right)

    def postOrderRecurse(self, root):
        if root:
            self.postOrderRecurse(root.left)
            self.postOrderRecurse(root.right)
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
        s = []
        r = root
        while r or len(s):
            if r:
                print(r.data)
                if(r.right):
                    s.append(r.right)
                r = r.left
            else:
                r = s.pop()

    def postOrderIterate(self, root):
        r = root
        s = []
        while r or len(s):
            if r:
                s.append(r)
                r = r.left
            else:
                n = s[-1].right
                if n:
                    r = n
                else:
                    n = s.pop()
                    print(n.data)
                    while len(s) and s[-1].right == n:
                        n = s.pop()
                        print(n.data)

    def _ifRightChild(self, node, stack):
        s = stack[-1]
        res = True
        if s.right:
            res = s.right.data == node.data
        return res


t = BinarySearchTree()
t.insert(t.root, 10)
t.insert(t.root, 8)
t.insert(t.root, 110)
t.insert(t.root, 8)
t.insert(t.root, 4)
t.insert(t.root, 11)
t.insert(t.root, 7)

