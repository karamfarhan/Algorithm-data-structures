
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










