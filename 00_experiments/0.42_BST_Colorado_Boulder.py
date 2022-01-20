"""
Trees and Graphs: Basics by University of Colorado Boulder
Week 1: Binary Search Trees
https://www.coursera.org/learn/trees-graphs-basics/home/welcome
"""

class Node:
    # Implement a node of the binary search tree.
    # Constructor for a node with key and a given parent
    # parent can be None for a root node.
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.left = None  # We will set left and right child to None
        self.right = None
        # Make sure that the parent's left/right pointer
        # will point to the newly created node.
        if parent is not None:
            if key < parent.key:
                assert (parent.left is None), 'parent already has a left child -- unable to create node'
                parent.left = self
            else:
                assert key > parent.key, 'key is same as parent.key. We do not allow duplicate keys in a BST since it breaks some of the algorithms.'
                assert (parent.right is None), 'parent already has a right child -- unable to create node'
                parent.right = self

    # Utility function that keeps traversing left until it finds
    # the leftmost descendant
    def get_leftmost_descendant(self):
        if self.left is not None:
            return self.left.get_leftmost_descendant()
        else:
            return self

    # TODO: Complete the search algorithm below
    # You can call search recursively on left or right child
    # as appropriate.
    # If search succeeds: return a tuple True and the node in the tree
    # with the key we are searching for.
    # Also note that if the search fails to find the key
    # you should return a tuple False and the node which would
    # be the parent if we were to insert the key subsequently.
    def search(self, key):
        if self.key == key:
            return True, self
        elif key < self.key:
            if self.left is None:
                return False, self
            else:
                return self.left.search(key)
        elif key > self.key:
            if self.right is None:
                return False, self
            else:
                return self.right.search(key)

    # TODO: Complete the insert algorithm below
    # To insert first search for it and find out
    # the parent whose child the currently inserted key will be.
    # Create a new node with that key and insert.
    # return None if key already exists in the tree.
    # return the new node corresponding to the inserted key otherwise.
    def insert(self, key):
        found, node = self.search(key)
        if found:
            return None
        else:
            if key < node.key:
                node.left = Node(key, node)
                return node.left
            elif key > node.key:
                node.right = Node(key, node)
                return node.right

    # height of a node whose children are both None is defined
    # to be 1.
    # height of any other node is 1 + maximum of the height
    # of its children.
    # Return a number that is th eheight.
    def height(self):
        if self is None:
            return 0
        else:
            left_subtree_height = self.left.height() if self.left is not None else 0
            right_subtree_height = self.right.height() if self.right is not None else 0
            return 1 + max(left_subtree_height, right_subtree_height)

    # TODO: Write an algorithm to delete a key in the tree.
    # First, find the node in the tree with the key.
    # Recommend drawing pictures to visualize these cases below before
    # programming.
    # Case 1: both children of the node are None
    #   -- in this case, deletion is easy: simply find out if the node with key is its
    #      parent's left/right child and set the corr. child to None in the parent node.
    # Case 2: one of the child is None and the other is not.
    #   -- replace the node with its only child. In other words,
    #      modify the parent of the child to be the to be deleted node's parent.
    #      also change the parent's left/right child appropriately.
    # Case 3: both children of the parent are not None.
    #    -- first find its successor (go one step right and all the way to the left).
    #    -- function get_leftmost_descendant may be helpful here.
    #    -- replace the key of the node by its successor.
    #    -- delete the successor node.
    # return: no return value specified

    def delete(self, key):
        (found, node_to_delete) = self.search(key)
        assert (found is True), f"key to be deleted:{key} - does not exist in the tree"
        if node_to_delete.parent is None:  # node_to_delete is root node



        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete.parent is not None:
                if node_to_delete.parent.left is node_to_delete:
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None
            else:  # node_to_delete.parent is None, so node_to_delete is root
                self = None
        elif (node_to_delete.left is None and node_to_delete.right is not None) \
                or (node_to_delete.left is not None and node_to_delete.right is None):
            pass







if __name__ == '__main__':
    t1 = Node(25, None)
    t2 = Node(12, t1)
    t3 = Node(18, t2)
    t4 = Node(40, t1)

    print('-- Testing basic node construction (originally provided code) -- ')
    assert (t1.left == t2), 'test 1 failed'
    assert (t2.parent == t1), 'test 2 failed'
    assert (t2.right == t3), 'test 3 failed'
    assert (t3.parent == t2), 'test 4 failed'
    assert (t1.right == t4), 'test 5 failed'
    assert (t4.left == None), 'test 6 failed'
    assert (t4.right == None), 'test 7 failed'
    # The tree should be :
    #             25
    #             /\
    #         12     40
    #         /\
    #     None  18
    #

    print('-- Testing search -- ')
    (b, found_node) = t1.search(18)
    assert b and found_node.key == 18, 'test 8 failed'
    (b, found_node) = t1.search(25)
    assert b and found_node.key == 25, 'test 9 failed -- you should find the node with key 25 which is the root'
    (b, found_node) = t1.search(26)
    assert (not b), 'test 10 failed'
    assert (
                found_node.key == 40), 'test 11 failed -- you should be returning the leaf node which would be the parent to the node you failed to find if it were to be inserted in the tree.'

    print('-- Testing insert -- ')
    ins_node = t1.insert(26)
    assert ins_node.key == 26, ' test 12 failed '
    assert ins_node.parent == t4, ' test 13 failed '
    assert t4.left == ins_node, ' test 14 failed '

    ins_node2 = t1.insert(33)
    assert ins_node2.key == 33, 'test 15 failed'
    assert ins_node2.parent == ins_node, 'test 16 failed'
    assert ins_node.right == ins_node2, 'test 17 failed'

    print('-- Testing height -- ')

    assert t1.height() == 4, 'test 18 failed'
    assert t4.height() == 3, 'test 19 failed'
    assert t2.height() == 2, 'test 20 failed'

    print('Success: 15 points.')