from .myLinkedList import MyLinkedList


class MyStack:
    def __init__(self):
        self.llist = MyLinkedList()

    def __iter__(self):
        return self.llist.__iter__()

    def __str__(self):
        return self.llist.__str__()

    def __len__(self):
        return len(self.llist)

    def peek(self):
        n = self.llist.first
        if n is None:
            return None
        return n.value

    def push(self, value):
        return self.llist.add_first(value)

    def pop(self):
        n = self.llist.remove_first()
        if n is None:
            return None
        return n.value
