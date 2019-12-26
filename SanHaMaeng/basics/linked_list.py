import unittest

from node import Node
'''
Within the LinkedList class, there are only
1) four references and
2) the number of data points to the node.
'''


class LinkedList:
    def __init__(self):
        '''
    Reduce the amount of if statements by placing dummy at the beginning.
    dummy: Nonsensical node that are put in front for ease of implementation,
          not nodes with actual data.
    '''
        dummy = Node('dummy')
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before

        self.num_of_data -= 1

        return pop_data

    def first(self):
        if self.num_of_data == 0:
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data

    def next(self):
        if self.current.next is None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.num_of_data

    def __del__(self):
        pass


class LinkedListTest(unittest.TestCase):
    def setUp(self):
        self.l_list = LinkedList()
        self.l_list.append(5)
        self.l_list.append(2)
        self.l_list.append(1)
        self.l_list.append(2)
        self.l_list.append(7)
        self.l_list.append(2)
        self.l_list.append(11)

    def testFirst(self):
        first = self.l_list.first()
        self.assertEqual(first, 5)

        next = self.l_list.next()
        self.assertEqual(next, 2)

        size = self.l_list.size()
        self.assertEqual(size, 7)

    def testDelete(self):
        delete = self.l_list.delete()
        self.assertEqual(delete, 2)

        size = self.l_list.size()
        self.assertEqual(size, 6)

    def testCurrent(self):
        current = self.l_list.current.data
        self.assertEqual(current, 5)

    def testTail(self):
        tail = self.l_list.tail.data
        self.assertEqual(tail, 11)

        first = self.l_list.first()
        self.assertEqual(first, 5)

        next = self.l_list.next()
        self.assertEqual(next, 1)

        next = self.l_list.next()
        self.assertEqual(next, 2)

        next = self.l_list.next()
        self.assertEqual(next, 7)


if __name__ == '__main__':
    unittest.main()
