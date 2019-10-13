from trees.bstNode import BstNode


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
                        r.left = BstNode(item, None, None, r)
                        break

                elif r.data < item:
                    if r.right:
                        r = r.right
                    else:
                        r.right = BstNode(item, None, None, r)
                        break
        else:
            self.root = BstNode(item, None, None, None)

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

    def treeMin(self, root):
        if not root:
            print('root empty')
            return 0
        r = root
        while r.left:
            r = r.left
        return r.data

    def treeMax(self, root):
        if not root:
            print('root empty')
            return 0
        r = root
        while r.right:
            r = r.right
        return r.data

    def _ifRightChild(self, BstNode, stack):
        s = stack[-1]
        res = True
        if s.right:
            res = s.right.data == BstNode.data
        return res

    def successor(self, BstNode):
        if not BstNode:
            print('BstNode empty')
            return
        if BstNode.right:
            return self.treeMin(BstNode.right)
        else:
            p = BstNode.parent
            while p:
                if BstNode != p.right:
                    break
                BstNode = p
                p = BstNode.parent
            return p

    def predecessor(self, BstNode):
        if not BstNode:
            print('BstNode empty')
            return
        if BstNode.left:
            return self.treeMax(BstNode.left)
        else:
            p = BstNode.parent
            while p:
                if BstNode != p.left:
                    break
                BstNode = p
                p = BstNode.parent
            return p

    def helperVOT(self, node, verticalOrder, nodeHeight, resHash):
        if not node:
            return
        if verticalOrder in resHash:
            resHash[verticalOrder].append((node.data, nodeHeight))
        else:
            resHash[verticalOrder] = [(node.data, nodeHeight)]
        self.helperVOT(node.left, verticalOrder-1, nodeHeight+1, resHash)
        self.helperVOT(node.right, verticalOrder+1, nodeHeight+1, resHash)

    def verticalOrderTraversal(self, root, rootHeight):
        if not self.root:
            return
        res = {}
        rootHeight = 0
        rootVertical = 0
        self.helperVOT(root, rootVertical, rootHeight, res)
        keys = list(res.keys())
        keys.sort()
        for i in res:
            res[i].sort(key=lambda tup: tup[1])
        print(*[res[i][0][0] for i in keys])

