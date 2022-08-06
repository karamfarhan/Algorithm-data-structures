# implement of hashtable in python


class hash_table:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for leter in key:
            hash += ord(leter)
        return hash % self.max

    def set_item(self, key, val):
        h = self.get_hash(key)
        found = False
        for inx, item in enumerate(self.arr[h]):
            if len(item) == 2 and item[0] == key:
                self.arr[h][inx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    def get_item(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                print(element[1])

    def delet_item(self, key):
        h = self.get_hash(key)
        for inx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][inx]


# test code
########################################
myhash = hash_table()
myhash.set_item("march 6", 100)
myhash.set_item("march 6", 200)
myhash.set_item("march 8", 500)
myhash.set_item("march 17", 700)
myhash.get_item("march 6")
myhash.delet_item("march 8")


# for i in myhash.arr:

#     print (i)
