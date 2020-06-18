from collections import Sequence
from enum import Enum


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


class MyLinkedList(Sequence):
    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
        self.direction = Direction.FORWARD

    def __len__(self) -> int:
        return self.count

    def __getitem__(self, index: int):
        if isinstance(index, slice):
            _list = MyLinkedList()
            _i = 0
            current = self.first
            while current is not None:
                if index.start >= _i >= index.stop:
                    _list.add_last(current.value)
                current = current.next
                _i += index.step
            return _list
        _i = 0
        current = self.first
        while current is not None:
            if _i == index:
                return current
            current = current.next
            _i += 1
        raise IndexError

    def __setitem__(self, key: int, value):
        self.__getitem__(key).value = value

    def __delitem__(self, index: int) -> MyLinkedListNode:
        node = self.__getitem__(index)
        self.remove(node)

    def __contains__(self, value):
        if self.find(value) is None:
            return False
        return True

    def __iter__(self):
        if self.direction == Direction.FORWARD:
            return MyLinkedListForwardIterator(self.first)
        if self.direction == Direction.BACKWARD:
            return MyLinkedListBackwardIterator(self.last)
        # should never reach this point
        return MyLinkedListForwardIterator(self.first)

    def __str__(self):
        s = '['
        current = self.first
        while current is not None:
            # TODO: fix last element's <->
            s += '(' + current.value + ') <-> '
            current = current.next
        s += ']'
        return s

    def find(self, value, startAt=0):
        occurrence = 0
        current = self.first
        while current is not None:
            if current.value == value:
                if occurrence == startAt:
                    return current
                occurrence += 1
            current = current.next
        return None

    def remove_first(self):
        if self.first is None:
            return None
        first = MyLinkedListNode(self.first.value)
        # the first element is also the last
        if self.first.next is None:
            self.first = None
            self.last = None
            self.count -= 1
            return first
        # remove dependency
        self.first.next.prev = None
        # set new head to its child
        self.first = self.first.next
        # remove head
        self.count -= 1
        # remove deps from a copy
        first.next = None
        return first

    def remove_last(self):
        if self.last is None:
            return None
        last = MyLinkedListNode(self.last.value)
        # the first element is also the last
        if self.last.prev is None:
            self.first = None
            self.last = None
            self.count -= 1
            return last
        # remove dependency
        self.last.prev.next = None
        # reset last link
        self.last = self.last.prev
        # remove last element
        self.count -= 1
        last.prev = None
        return last

    def remove(self, node: MyLinkedListNode):
        if self.first is None:
            return None

        # There are 3 cases:
        # 1) head is set to remove
        # 2) last element (tail) is set to remove
        # 3) element with child and parent is set to remove
        # case 1 Removing head
        if node == self.first:
            return self.remove_first()
        if node == self.last:
            return self.remove_last()

        # case 3 Removing regular element
        # Example: remove 5 in (3)<->(5)<->(2)
        # (5).prev = (5).next
        # which is (3)->(2)
        node.prev = node.next
        # (5).next.prev = (5).prev
        # which is (3)<->(2)
        node.next.prev = node.prev
        # now securely remove
        self.count -= 1
        return node

    def add_first(self, value):
        return self.add_first_node(MyLinkedListNode(value))

    def add_first_node(self, node):
        if self.first is None:
            self.first = node
            self.first.origin = self
            self.last = self.first
        else:
            node.next = self.first
            self.first.prev = node
            self.first = node
            self.first.origin = self

        self.count += 1
        return self.first

    def add_last(self, value):
        return self.add_last_node(MyLinkedListNode(value))

    def add_last_node(self, node: MyLinkedListNode):
        if self.first is None:
            self.first = node
            self.first.origin = self
            self.last = self.first
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.count += 1
        return self.last

    def add_before(self, value1, value2):
        node1 = self.find(value1)
        node2 = MyLinkedListNode(value2)
        return self.add_before_node_node(node1, node2)

    def add_before_node_value(self, node1: MyLinkedListNode, value):
        node2 = MyLinkedListNode(value)
        return self.add_before_node_node(node1, node2)

    def add_before_node_node(self, node1: MyLinkedListNode, node2: MyLinkedListNode):
        if node2 is None:
            return None
        if self.first is None:
            return None
        if node1 is None:
            return None
        if self.first == node1:
            return self.add_first_node(node2)

        current = self.first
        while current is not None:
            if current != node1:
                current = current.next
                continue
            break
        if current is None:
            return None
        # Example: insert(5)
        # before(2) in (3) <->(2)
        # current = (2)
        node2.prev = current.prev
        # (3) < -(5)(2)
        current.prev = node2
        # (3) < -(5) < -(2)
        node2.next = current
        # (3) < -(5) <->(2)
        node2.prev.next = node2
        # (3) <->(5) <->(2)
        node2.origin = self
        self.count += 1
        return node2

    def add_after(self, value1, value2):
        node1 = self.find(value1)
        node2 = MyLinkedListNode(value2)
        return self.add_after_node_node(node1, node2)

    def add_after_node_value(self, node1: MyLinkedListNode, value):
        node2 = MyLinkedListNode(value)
        return self.add_after_node_node(node1, node2)

    def add_after_node_node(self, node1: MyLinkedListNode, node2: MyLinkedListNode):
        if node2 is None:
            return None
        if self.first is None:
            return None
        if node1 is None:
            return None

        current = self.first
        while current is not None:
            if current != node1:
                current = current.next
                continue
            break
        if current is None:
            return None

        # Example: insert 5 after (3) in (3)<->(2)
        # current = (3)
        # Case where node is found and it is last element
        if current.next is None:
            return self.add_last_node(node2)
        node2.next = current.next
        # (3)(5)->(2)
        # ^ --------- |
        node2.prev = current
        # (3) < -(5)->(2)
        # ^ ---------- |
        node2.next.prev = node2
        # (3) < -(5) <->(2)
        node2.prev.next = node2
        # (3) <->(5) <->(2)
        node2.origin = self
        self.count += 1
        return node2


class MyLinkedListForwardIterator:
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


class MyLinkedListBackwardIterator:
    def __init__(self, node: MyLinkedListNode):
        self.current = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.prev
        return value


class Direction(Enum):
    FORWARD = 1,
    BACKWARD = 2
