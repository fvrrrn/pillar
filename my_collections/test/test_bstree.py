from unittest import TestCase
from my_collections.bstree import BSTree
from my_collections.bstree import BSTreeNode

class TestBSTree(TestCase):
    def test_getitem(self):
        t = BSTree()
        n1 = BSTreeNode(0)
        n2 = BSTreeNode(1)
        t.add_node(n1)
        t.add_node(n2)
        with self.assertRaises(IndexError):
            e = t[0:1]
        self.assertEqual(t[0], n1)
        self.assertEqual(t[0], t.root)
        self.assertEqual(t[1], n2)
        self.assertEqual(t[1], t.root.right)

    def test_contains(self):
        t = BSTree()
        v1 = 1
        v2 = 2
        t.add(v1)
        self.assertTrue(v1 in t)
        self.assertFalse(v2 in t)

    def test_add(self):
        t = BSTree()
        self.assertIsNone(t.root)
        self.assertEqual(len(t), 0)
        v1 = 5
        self.assertEqual(t.add(v1).value, v1)
        self.assertEqual(t.root.value, v1)
        self.assertEqual(len(t), 1)
        v2 = 2
        self.assertEqual(t.add(v2).value, v2)
        self.assertNotEqual(t.root.value, v2)
        self.assertEqual(len(t), 2)
        v3 = 2
        self.assertIsNone(t.add(v3))
        self.assertEqual(len(t), 2)

    def test_add_node(self):
        t = BSTree()
        self.assertIsNone(t.root)
        self.assertEqual(len(t), 0)
        n1 = BSTreeNode(5)
        self.assertEqual(t.add_node(n1), n1)
        self.assertEqual(t.root, n1)
        self.assertEqual(len(t), 1)
        self.assertEqual(t, n1.origin)
        n2 = BSTreeNode(2)
        self.assertEqual(t.add_node(n2), n2)
        self.assertNotEqual(t.root, n2)
        self.assertEqual(len(t), 2)
        self.assertEqual(n2.parent, t.root)
        self.assertEqual(t.root.left, n2)
        self.assertEqual(t.root.left.parent, t.root)
        self.assertEqual(t, n2.origin)
        n3 = BSTreeNode(6)
        self.assertEqual(t.add_node(n3), n3)
        self.assertNotEqual(t.root, n3)
        self.assertEqual(len(t), 3)
        self.assertEqual(n3.parent, t.root)
        self.assertEqual(t.root.right, n3)
        self.assertEqual(t.root.right.parent, t.root)
        self.assertEqual(t, n3.origin)
        n4 = BSTreeNode(4)
        self.assertEqual(t.add_node(n4), n4)
        self.assertNotEqual(t.root, n4)
        self.assertEqual(len(t), 4)
        self.assertEqual(n4.parent, n2)
        self.assertEqual(n2.right, n4)
        self.assertEqual(t.root.left.right, n4)
        self.assertEqual(t.root.left.right.parent, n2)
        self.assertEqual(t, n4.origin)

    def test_remove_node(self):
        t = BSTree()
        n1 = BSTreeNode(5)
        self.assertIsNone(t.remove_node(None))
        t.add_node(n1)
        self.assertEqual(len(t), 1)
        self.assertEqual(t.root, n1)
        self.assertEqual(t.root.origin, t)
        self.assertEqual(t.remove_node(n1), n1)
        self.assertEqual(len(t), 0)
        self.assertIsNone(t.root)
        self.assertIsNone(n1.origin)
        n2 = BSTreeNode(4)
        t.add_node(n1)
        t.add_node(n2)
        for n in t:
            print(n.value)



class TestBSTreeNode(TestCase):
    def test_has_right_child(self):
        n1 = BSTreeNode(1)
        self.assertIsNone(n1.right)
        n2 = BSTreeNode(2)
        n1.right = n2
        self.assertEqual(n1.right, n2)


    def test_has_left_child(self):
        n1 = BSTreeNode(1)
        self.assertIsNone(n1.left)
        n2 = BSTreeNode(2)
        n1.left = n2
        self.assertEqual(n1.left, n2)

    def test_child_amout(self):
        n1 = BSTreeNode(1)
        n2 = BSTreeNode(2)
        n3 = BSTreeNode(3)
        n1.right = n2
        self.assertEqual(n1.child_amout(), 1)
        n1.left = n3
        self.assertEqual(n1.child_amout(), 2)


    def test_is_right_child(self):
        n1 = BSTreeNode(1)
        n2 = BSTreeNode(2)
        self.assertFalse(n1.is_right_child())
        n1.parent = n2
        self.assertFalse(n1.is_right_child())
        n2.right = n1
        self.assertTrue(n1.is_right_child())


    def test_is_left_child(self):
        n1 = BSTreeNode(1)
        n2 = BSTreeNode(2)
        self.assertFalse(n1.is_left_child())
        n1.parent = n2
        self.assertFalse(n1.is_left_child())
        n2.left = n1
        self.assertTrue(n1.is_left_child())

    def test_is_leaf(self):
        n1 = BSTreeNode(1)
        self.assertTrue(n1.is_leaf())
        n2 = BSTreeNode(2)
        n1.right = n2
        self.assertFalse(n1.is_leaf())
        n3 = BSTreeNode(3)
        n2.left = n3
        self.assertFalse(n2.is_leaf())