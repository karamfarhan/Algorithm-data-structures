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







