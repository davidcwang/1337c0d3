"""
Problem: 297. Serialize and Deserialize Binary Tree
Url: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Author: David Wang
Date: 05/28/2019
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if root == None:
            return []

        queue = [root]
        data = []
        while queue:
            node = queue.pop(0)
            if node != None:
                data.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                data.append(None)

        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: List[TreeNode]
        :rtype: TreeNode
        """
        if not data:
            return None
        root = TreeNode(data.pop(0))
        queue = [root]
        index = 0
        while queue:
            node = queue.pop(0)

            left = data[index]
            index += 1
            right = data[index]
            index += 1


            if left != None:
                lNode = TreeNode(left)
                queue.append(lNode)
                node.left = lNode
            else:
                node.left = None
            if right != None:
                rNode = TreeNode(right)
                queue.append(rNode)
                node.right = rNode
            else:
                node.right = None

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    in_data = [1,2,3,None,None,4,5]
    root = Codec().deserialize(in_data)
    data = Codec().serialize(root)
    print('input: {}'.format(in_data))
    print('root: {}'.format(root))
    print('data: {}'.format(data))

    in_data = []
    root = Codec().deserialize(in_data)
    data = Codec().serialize(root)
    print('input: {}'.format(in_data))
    print('root: {}'.format(root))
    print('data: {}'.format(data))

    in_data = [-1,0,1]
    root = Codec().deserialize(in_data)
    data = Codec().serialize(root)
    print('input: {}'.format(in_data))
    print('root: {}'.format(root))
    print('data: {}'.format(data))
