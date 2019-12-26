'''
A node consists of data and a reference to the next node.
If the node does not point to the next node, it is the end of the list.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        pass
