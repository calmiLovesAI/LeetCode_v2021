# Leetcode: https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
# 二叉树的序列化和反序列化

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("Null")
        return "[" + ",".join(res) + "]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        dataList = data[1:-1].split(",")
        root = TreeNode(int(dataList[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if dataList[i] != "Null":
                node.left = TreeNode(int(dataList[i]))
                q.append(node.left)
            i += 1
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                q.append(node.right)
            i += 1
        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
