# first we have to make a class for the nodes
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# then we makes a class for the linked list and give it a head wich in the first  = none
class LinkedList:
    def __init__(self):
        self.head = None

    # to insert the nods at the begin (make it the head of the linked list)

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    # for insert the node at the end of the linked list
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    # to make a linked list a given list

    def insert_valuse(self, data_list):
        self.head = None
        for i in data_list:
            self.insert_at_end(i)

    # to return the lenth of the linked list

    def lenth(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # to remove element at a given index

    def remove_at(self, index):
        if index < 0 or index > self.lenth():
            raise Exception("invilid index")
        if index == 0:
            self.head = self.head.next

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    # to insert elemrent at a given index

    def insert_at(self, index, data):
        if index < 0 or index > self.lenth():
            raise Exception("invilid index")

        if index == 0:
            self.insert_at_begin(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    # to get the value from a given index

    def get_data_at(self, index):
        if index < 0 or index > self.lenth():
            raise Exception("invilid index ")

        count_index = 0
        itr = self.head
        while itr:
            if count_index == index:
                return itr.data
            itr = itr.next
            count_index += 1

    # to insert value after some value (not index):

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            node = Node(data_to_insert, None)
            self.head = Node(data_after, node)
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    # to remove any value by the name of the value not the index
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr:
            if itr.next is None:
                print("the linked list have not data like this")
                break
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next

    # to reverse the linked list (by reverse the next for the nodes to the last node behind it)
    def reverse_linked(self):
        curr = self.head
        last = None
        while True:
            next = curr.next
            curr.next = last
            if next is None:
                break
            last = curr
            curr = next

        # now we can print it to see
        itr = curr
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    # this def to help us print the linkden list

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return

        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)


# Some test code for the linked list

if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_end(1)
    # ll.insert_at_end(2)
    # ll.insert_at_end(3)
    # ll.insert_at_end(4)
    # ll.insert_at_end(5)

    # ll.print()
    # ll.reverse_linked()
    ########

    # ll.insert_at_begin(5)
    # ll.insert_at_begin(89)

    # ll.insert_at_end(3)
    # ll.insert_at_end(7)

    # print (ll.lenth())

    # ll.remove_at(0)

    # ll.insert_at(2, "orang")

    # lis = ["banana","mango","graps","orang"]
    # ll.insert_valuse(lis)

    # ll.insert_after_value("mango", "apple")

    # ll.remove_by_value("banana")

    # print(ll.get_data_at(2))

    # print (ll.get_data_at(ll.lenth()-1))

    # ll.print()

    # for test to the tmaren *************
    # ll = LinkedList()
    # ll.insert_valuse(["banana","mango","grapes","orange"])
    # ll.print()
    # ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.print()
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.print()
    # ll.remove_by_value("figs")
    # ll.print()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print()
