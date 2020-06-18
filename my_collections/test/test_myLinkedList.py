from unittest import TestCase
from my_collections.myLinkedList import MyLinkedList
from my_collections.myLinkedList import MyLinkedListNode


class TestMyLinkedList(TestCase):
    def test_find(self):
        l = MyLinkedList()
        self.assertIsNone(l.find(0))
        v1 = 1
        n1 = MyLinkedListNode(v1)
        l.add_last_node(n1)
        self.assertEqual(n1, l.find(v1))
        self.assertEqual(n1.value, l.find(v1).value)
        self.assertEqual(v1, l.find(v1).value)
        v2 = 2
        n2 = MyLinkedListNode(v2)
        l.add_last_node(n2)
        self.assertEqual(n2, l.find(v2))
        self.assertEqual(n2.value, l.find(v2).value)
        self.assertEqual(v2, l.find(v2).value)
        v3 = 2
        n3 = MyLinkedListNode(v3)
        l.add_last_node(n3)
        self.assertNotEqual(n3, l.find(v3))
        self.assertEqual(n2, l.find(v3))
        self.assertEqual(n2.value, l.find(v3).value)
        self.assertEqual(v3, l.find(v3).value)
        self.assertEqual(v2, l.find(v2).value)
        self.assertEqual(n3, l.find(v3, startAt=1))
        self.assertNotEqual(n2, l.find(v3, startAt=1))
        self.assertEqual(n2.value, l.find(v3, startAt=1).value)
        self.assertEqual(v3, l.find(v3, startAt=1).value)
        self.assertEqual(v2, l.find(v2, startAt=1).value)

    def test_remove_first(self):
        l = MyLinkedList()
        v1 = 1
        v2 = 2
        self.assertEqual(0, len(l))
        self.assertIsNone(l.remove_first())
        l.add_last(v1)
        self.assertEqual(1, len(l))
        self.assertEqual(v1, l.remove_first().value)
        self.assertEqual(0, len(l))
        l.add_last(v1)
        l.add_last(v2)
        self.assertEqual(2, len(l))
        self.assertEqual(v1, l.remove_first().value)
        self.assertEqual(1, len(l))

    def test_remove_last(self):
        l = MyLinkedList()
        v1 = 1
        v2 = 2
        self.assertEqual(0, len(l))
        self.assertIsNone(l.remove_last())
        l.add_last(v1)
        self.assertEqual(1, len(l))
        self.assertEqual(v1, l.remove_last().value)
        self.assertEqual(0, len(l))
        l.add_last(v1)
        l.add_last(v2)
        self.assertEqual(2, len(l))
        self.assertEqual(v2, l.remove_last().value)
        self.assertEqual(1, len(l))

    # TODO: add slicing test

    def test_remove(self):
        l = MyLinkedList()
        v1 = 1
        v2 = 2
        v3 = 3
        self.assertEqual(0, len(l))
        with self.assertRaises(IndexError):
            del l[0]
        l.add_last(v1)
        self.assertEqual(1, len(l))
        del l[0]
        self.assertEqual(0, len(l))
        l.add_last(v1)
        l.add_last(v2)
        self.assertEqual(2, len(l))
        del l[1]
        self.assertEqual(v1, l[0].value)

    def test_add_first(self):
        l = MyLinkedList()
        v1 = 1
        v2 = 2
        self.assertEqual(0, len(l))
        self.assertEqual(v1, l.add_first(v1).value)
        self.assertEqual(v1, l.first.value)
        self.assertEqual(v1, l.last.value)
        self.assertEqual(1, len(l))
        self.assertEqual(v2, l.add_first(v2).value)
        self.assertEqual(v2, l.first.value)
        self.assertEqual(v1, l.last.value)
        self.assertEqual(2, len(l))

    def test_add_first_node(self):
        l = MyLinkedList()
        v1 = 1
        v2 = 2
        n1 = MyLinkedListNode(v1)
        n2 = MyLinkedListNode(v2)
        self.assertEqual(0, len(l))
        self.assertEqual(n1, l.add_first_node(n1))
        self.assertEqual(n1, l.first)
        self.assertEqual(n1, l.last)
        self.assertEqual(v1, l.first.value)
        self.assertEqual(v1, l.last.value)
        self.assertEqual(1, len(l))
        self.assertEqual(n2, l.add_first_node(n2))
        self.assertEqual(n2, l.first)
        self.assertEqual(n1, l.last)
        self.assertEqual(v2, l.first.value)
        self.assertEqual(v1, l.last.value)
        self.assertEqual(2, len(l))

    def test_add_last(self):
        l = MyLinkedList()
        v1 = 1
        v2 = 2
        self.assertEqual(0, len(l))
        self.assertEqual(v1, l.add_last(v1).value)
        self.assertEqual(v1, l.first.value)
        self.assertEqual(v1, l.last.value)
        self.assertEqual(1, len(l))
        self.assertEqual(v2, l.add_last(v2).value)
        self.assertEqual(v1, l.first.value)
        self.assertEqual(v2, l.last.value)
        self.assertEqual(2, len(l))

    def test_add_last_node(self):
        l = MyLinkedList()
        v1 = 1
        v2 = 2
        n1 = MyLinkedListNode(v1)
        n2 = MyLinkedListNode(v2)
        self.assertEqual(0, len(l))
        self.assertEqual(n1, l.add_last_node(n1))
        self.assertEqual(n1, l.first)
        self.assertEqual(n1, l.last)
        self.assertEqual(v1, l.first.value)
        self.assertEqual(v1, l.last.value)
        self.assertEqual(1, len(l))
        self.assertEqual(n2, l.add_last_node(n2))
        self.assertEqual(n1, l.first)
        self.assertEqual(n2, l.last)
        self.assertEqual(v1, l.first.value)
        self.assertEqual(v2, l.last.value)
        self.assertEqual(2, len(l))

    def test_add_before(self):
        l = MyLinkedList()
        self.assertIsNone(l.add_before(None, None))
        v1 = 1
        self.assertIsNone(l.add_before(v1, None))
        v2 = 2
        self.assertIsNone(l.add_before(None, v2))
        self.assertIsNone(l.add_before(v1, v2))
        self.assertEqual(0, len(l))
        l.add_last(v1)
        self.assertEqual(1, len(l))
        self.assertEqual(v2, l.add_before(v1, v2).value)
        self.assertEqual(2, len(l))
        self.assertEqual(v2, l.first.value)
        self.assertEqual(v1, l.last.value)
        v3 = 3
        self.assertEqual(v3, l.add_before(v1, v3).value)
        self.assertEqual(3, len(l))
        self.assertEqual(v2, l.first.value)
        self.assertEqual(v1, l.last.value)
        self.assertEqual(v3, l[1].value)
        l.add_first(v2)
        self.assertEqual(v2, l[1].value)
        v4 = 4
        self.assertEqual(v4, l.add_before(v2, v4).value)
        self.assertEqual(5, len(l))
        self.assertEqual(v1, l.last.value)
        self.assertEqual(v2, l[2].value)
        self.assertEqual(v3, l[3].value)
        self.assertEqual(v4, l.first.value)

    def test_add_before_node_value(self):
        l = MyLinkedList()
        self.assertIsNone(l.add_before_node_value(None, None))
        v1 = 1
        n1 = MyLinkedListNode(v1)
        self.assertIsNone(l.add_before_node_value(n1, None))
        v2 = 2
        self.assertIsNone(l.add_before_node_value(None, v2))
        self.assertIsNone(l.add_before_node_value(n1, v2))
        self.assertEqual(0, len(l))
        l.add_last_node(n1)
        self.assertEqual(1, len(l))
        self.assertEqual(v2, l.add_before_node_value(n1, v2).value)
        self.assertEqual(2, len(l))
        self.assertEqual(n1, l.last)
        self.assertEqual(v2, l.first.value)
        v3 = 3
        self.assertEqual(v3, l.add_before_node_value(n1, v3).value)
        self.assertEqual(3, len(l))
        self.assertEqual(n1, l[2])
        self.assertEqual(v3, l[1].value)
        self.assertEqual(v2, l.first.value)

    def test_add_before_node_node(self):
        l = MyLinkedList()
        self.assertIsNone(l.add_before_node_node(None, None))
        v1 = 1
        n1 = MyLinkedListNode(v1)
        self.assertIsNone(l.add_before_node_node(n1, None))
        v2 = 2
        n2 = MyLinkedListNode(v2)
        self.assertIsNone(l.add_before_node_node(None, n2))
        self.assertIsNone(l.add_before_node_node(n1, n2))
        self.assertEqual(0, len(l))
        l.add_last_node(n1)
        self.assertEqual(1, len(l))
        self.assertEqual(n2, l.add_before_node_node(n1, n2))
        self.assertEqual(2, len(l))
        self.assertEqual(n2, l.first)
        self.assertEqual(n1, l.last)
        v3 = 3
        n3 = MyLinkedListNode(v3)
        self.assertEqual(n3, l.add_before_node_node(n1, n3))
        self.assertEqual(3, len(l))
        self.assertEqual(n2, l.first)
        self.assertEqual(n1, l.last)
        self.assertEqual(n3, l[1])

    def test_add_after(self):
        l = MyLinkedList()
        self.assertIsNone(l.add_after(None, None))
        v1 = 1
        self.assertIsNone(l.add_after(v1, None))
        v2 = 2
        self.assertIsNone(l.add_after(None, v2))
        self.assertIsNone(l.add_after(v1, v2))
        self.assertEqual(0, len(l))
        l.add_last(v1)
        self.assertEqual(1, len(l))
        self.assertEqual(v2, l.add_after(v1, v2).value)
        self.assertEqual(2, len(l))
        self.assertEqual(v1, l.first.value)
        self.assertEqual(v2, l.last.value)
        v3 = 3
        self.assertEqual(v3, l.add_after(v1, v3).value)
        self.assertEqual(3, len(l))
        self.assertEqual(v1, l.first.value)
        self.assertEqual(v2, l.last.value)
        self.assertEqual(v3, l[1].value)
        l.add_last(v2)
        self.assertEqual(v2, l[len(l) - 1].value)
        v4 = 4
        self.assertEqual(v4, l.add_after(v2, v4).value)
        self.assertEqual(5, len(l))
        self.assertEqual(v1, l.first.value)
        self.assertEqual(v2, l.last.value)
        self.assertEqual(v2, l[len(l) - 3].value)
        self.assertEqual(v3, l[1].value)
        self.assertEqual(v4, l[len(l) - 2].value)

    def test_add_after_node_value(self):
        l = MyLinkedList()
        self.assertIsNone(l.add_after_node_value(None, None))
        v1 = 1
        n1 = MyLinkedListNode(v1)
        self.assertIsNone(l.add_after_node_value(n1, None))
        v2 = 2
        self.assertIsNone(l.add_after_node_value(None, v2))
        self.assertIsNone(l.add_after_node_value(n1, v2))
        self.assertEqual(0, len(l))
        l.add_last_node(n1)
        self.assertEqual(1, len(l))
        self.assertEqual(v2, l.add_after_node_value(n1, v2).value)
        self.assertEqual(2, len(l))
        self.assertEqual(n1, l.first)
        self.assertEqual(v2, l.last.value)
        v3 = 3
        self.assertEqual(v3, l.add_after_node_value(n1, v3).value)
        self.assertEqual(3, len(l))
        self.assertEqual(n1, l.first)
        self.assertEqual(v2, l.last.value)
        self.assertEqual(v3, l[1].value)

    def test_add_after_node_node(self):
        l = MyLinkedList()
        self.assertIsNone(l.add_after_node_node(None, None))
        v1 = 1
        n1 = MyLinkedListNode(v1)
        self.assertIsNone(l.add_after_node_node(n1, None))
        v2 = 2
        n2 = MyLinkedListNode(v2)
        self.assertIsNone(l.add_after_node_node(None, n2))
        self.assertIsNone(l.add_after_node_node(n1, n2))
        self.assertEqual(0, len(l))
        l.add_last_node(n1)
        self.assertEqual(1, len(l))
        self.assertEqual(n2, l.add_after_node_node(n1, n2))
        self.assertEqual(2, len(l))
        self.assertEqual(n1, l.first)
        self.assertEqual(n2, l.last)
        v3 = 3
        n3 = MyLinkedListNode(v3)
        self.assertEqual(n3, l.add_after_node_node(n1, n3))
        self.assertEqual(3, len(l))
        self.assertEqual(n1, l.first)
        self.assertEqual(n2, l.last)
        self.assertEqual(n3, l[1])
