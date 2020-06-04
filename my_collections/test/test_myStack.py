from my_collections.myStack import MyStack
from unittest import TestCase


class TestMyStack(TestCase):
    def test_peek(self):
        s = MyStack()
        self.assertIsNone(s.peek())
        s.push(1)
        s.push(2)
        self.assertEqual(2, len(s))
        self.assertEqual(2, s.peek())

    def test_push(self):
        s = MyStack()
        s.push(1)
        self.assertEqual(1, len(s))
        self.assertEqual(1, s.peek())

    def test_pop(self):
        s = MyStack()
        self.assertIsNone(s.pop())
        s.push(1)
        s.push(2)
        self.assertEqual(2, len(s))
        self.assertEqual(2, s.pop())
        self.assertEqual(1, len(s))
        self.assertEqual(1, s.peek())
