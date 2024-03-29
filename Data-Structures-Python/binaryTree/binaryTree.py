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

    # get the min node
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    # get the biggest node
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # sum of all the nodes
    def sum(self):
        nat = 0
        if self.left:
            nat += self.left.sum()
        if self.right:
            nat += self.right.sum()
        return nat + self.data


# helper function
def bulit_tree(my_list):
    root = binary_tree(my_list[0])
    for i in range(1, len(my_list)):
        root.add_child(my_list[i])
    return root


# test code
if __name__ == "__main__":

    my_list = [15, 12, 14, 7, 27, 20, 88]
    tree = bulit_tree(my_list)

    # print(tree.find_min())
    # print(tree.find_max())
    # print(tree.search(88))
    # print(tree.in_order())
    # print(tree.pre_order())
    # print(tree.pos_order())
    # print(tree.bfs())
    # tree.add_child(16)
    # print(tree.in_order())
    # tree.delet(16)
    # print(tree.in_order())
    # print(tree.sum())
