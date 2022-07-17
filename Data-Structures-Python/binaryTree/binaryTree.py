# impelement of binary tree in python

class binary_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    # add node 
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binary_tree(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binary_tree(data)
    # to search for specific node
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    # to delete node
    def delet(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delet(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delet(val)
        else:  # means you now in the val node
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delet(min_val)
        return self

    # depth first search
    def in_order(self):
        element = []
        if self.left:
            element += self.left.in_order()
        element.append(self.data)
        if self.right:
            element += self.right.in_order()
        return element

    # get in pre order
    def pre_order(self):
        element = []
        element.append(self.data)
        if self.left:
            element += self.left.pre_order()
        if self.right:
            element += self.right.pre_order()
        return element

    # get in post order
    def pos_order(self):
        element = []
        if self.left:
            element += self.left.pos_order()
        if self.right:
            element += self.right.pos_order()
        element.append(self.data)
        return element

    # BFS
    def bfs(self):
        nat = []
        qu = []
        qu.append(self)
        while len(qu) > 0:
            node = qu.pop(0)
            if node is not None:
                nat.append(node.data)
                qu.append(node.left)
                qu.append(node.right)
        return nat





