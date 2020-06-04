class MyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        self.origin = None

    def is_leaf(self):
        return self.prev is not None and self.next is None

    def is_internal(self):
        return self.prev is not None and self.next is not None
