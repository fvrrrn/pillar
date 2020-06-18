from collections import Sequence
from enum import Enum


class BSTree(Sequence):
    def __init__(self):
        self.root = None
        self.count = 0
        self.traversal_mode = TraversalMode.LNR

    def __len__(self) -> int:
        return self.count

    def __getitem__(self, value):
        if isinstance(value, slice):
            raise IndexError('slice is not supported.')
        node = self.root
        while node is not None:
            if value < node.value:
                node = node.left
                continue
            if value > node.value:
                node = node.right
                continue
            break
        return node

    def __delitem__(self, value):
        self.remove_node(self.__getitem__(value))

    def __contains__(self, value) -> bool:
        return self.__getitem__(value) is not None

    def __iter__(self):
        if self.traversal_mode == TraversalMode.LNR:
            return LNRIterator(self.root)

    def __str__(self) -> str:
        return (str)(n.value for n in self.__iter__())

    def add(self, value):
        return self.add_node(BSTreeNode(value))

    def add_node(self, node):
        if self.root is None:
            self.root = node
            self.count += 1
            self.root.origin = self
            return node

        if node.parent is None:
            node.parent = self.root

        if node.value < node.parent.value:
            if node.parent.left is None:
                node.parent.left = node
                self.count += 1
                node.origin = self
                return node
            node.parent = node.parent.left
            return self.add_node(node)

        if node.value > node.parent.value:
            if node.parent.right is None:
                node.parent.right = node
                self.count += 1
                node.origin = self
                return node
            node.parent = node.parent.right
            return self.add_node(node)
        return None

    def remove_node(self, node):
        if node is None or node.origin != self:
            return None

        was_head = node == self.root

        if self.count == 1:
            self.root = None
            node.origin = None
            self.count -= 1
            return node

        if node.is_leaf():
            if node.is_left_child:
                node.parent.left = None
            else:
                node.parent.right = None

            node.origin = None
            node.parent = None
            return node

        if node.child_amout() == 1:
            if node.has_left_child:
                if was_head:
                    self.root = node.left
                if node.is_left_child:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                return node
            if was_head:
                self.root = node.right
            if node.is_left_child:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            return node

        successor_node = node.Left
        while successor_node.right is not None:
            successor_node = successor_node.right
        node.value = successor_node.value
        self.remove_node(successor_node)
        return node


class BSTreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.parent = None
        self.origin = None

    def has_right_child(self):
        return self.right is not None

    def has_left_child(self):
        return self.left is not None

    def child_amout(self):
        a = 0
        if self.right is not None:
            a += 1
        if self.left is not None:
            a += 1
        return a

    def is_right_child(self):
        return self.parent is not None and self.parent.right == self

    def is_left_child(self):
        return self.parent is not None and self.parent.left == self

    def is_leaf(self):
        return self.left is None and self.right is None


class LNRIterator:
    def __init__(self, node):
        self.current = node

    def __iter__(self):
        while self.current is not None:

            if self.current.left is None:
                yield self.current.data
                self.current = self.current.right
            else:
                pre = self.current.left
                while pre.right is not None and pre.right is not self.current:
                    pre = pre.right

                if pre.right is None:
                    pre.right = self.current
                    self.current = self.current.left

                else:
                    pre.right = None
                    yield self.current.data
                    self.current = self.current.right


class TraversalMode(Enum):
    LNR = 1,
    NLR = 2,
    RNL = 3
