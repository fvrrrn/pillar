from abc import abstractmethod
from collections import Sequence

from .myLinkedListNode import MyLinkedListNode


class MyLinkedList(Sequence):
    def __len__(self) -> int:
        return self.count

    def __getitem__(self, index):
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

    def __setitem__(self, key, value):
        self.__getitem__(key).value = value

    def __delitem__(self, index):
        node = self.__getitem__(index)
        if self.first is None:
            return None

        # There are 3 cases:
        # 1) head is set to remove
        # 2) last element (tail) is set to remove
        # 3) element with child and parent is set to remove
        # case 1 Removing head
        if node == self.first:
            if self.first.next is None:
                self.first = None
                self.last = None
                self.count -= 1
                return node

            # creating temporary variable
            tmp = self.first.next
            # remove dependency
            tmp.prev = None
            # set new head to its child
            self.first = tmp
            # remove head
            self.count -= 1
            return node
            # case 2 Removing last element
        if node == self.last:
            # creating temporary variable
            tmp = self.last.prev
            # remove dependency
            tmp.next = None
            # reset last link
            self.last = tmp
            # remove last element
            self.count -= 1
            return node

        # current = self.first
        # while current is not None:
        #     if current != node:
        #         current = current.next
        #         continue
        #     break
        # if current is None:
        #     return None

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

    def __contains__(self, value):
        current = self.first
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def find(self, value, startAt=0):
        occurance = 0
        current = self.first
        while current is not None:
            if current.value:
                if occurance == startAt:
                    return current
                occurance += 1
            current = current.next
        return None

    def remove(self, value):
        if self.first is None:
            return None

        current = self.first
        while current is not None:
            if current.value != value:
                current = current.next
                continue
            break

        # no match found
        if current is None:
            return None

        # if head is last element
        if self.first.next is None:
            v = self.first.copy()
            self.first = None
            self.last = None
            self.count -= 1
            return v

        # There are 3 cases:
        # 1) head is set to remove
        # 2) last element (tail) is set to remove
        # 3) element with child and parent is set to remove
        # case 2 Removing last element
        if current.next is None:
            # remove dependency
            current.prev.next = None
            # reset last link
            self.last = current.prev
            # remove last element
            self.count -= 1
            return current

        # case 1 Removing head
        if current.prev is None:
            # remove dependency
            current.next.prev = None
            # set new head to its child
            self.first = current.next
            # remove head
            self.count -= 1
            return current

        # case 3 Removing regular element
        # Example: remove 5 in (3)<->(5)<->(2)
        # (5).prev = (5).next
        # which is (3)->(2)
        current.prev = current.next
        # (5).next.prev = (5).prev
        # which is (3)<->(2)
        current.next.prev = current.prev
        # now securely remove
        self.count -= 1
        return current



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

    def add_last_node(self, node):
        if self.first is None:
            self.first = node
            self.first.origin = self
            self.count += 1
            self.last = self.first
            return self.last
        else:
            self.last.next = node
            node.prev = self.last
            self.count += 1
            self.last = node
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
