"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        #because the children is not a linkined list just a list
        if not root : 
            return 0 
        elif not root.children :
            return 1
        else: 
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1 