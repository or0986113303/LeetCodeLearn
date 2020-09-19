# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def maketonode(self, source):
        if not source:
            return None
        middle = len(source) // 2
        result = TreeNode(val=source[middle])
        leftpart = self.maketonode(source[:middle])
        rightpart = self.maketonode(source[middle+1:])
        result.left = leftpart
        result.right = rightpart
        return result
    
    def maketolist(self, source, result):
        if not source:
            return
        
        self.maketolist(source.left, result)
        result.append(source.val)
        self.maketolist(source.right, result)
        
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if not root:
            return root
        
        sourcetmp = []
        self.maketolist(root, sourcetmp)
        print(sourcetmp)
        result = self.maketonode(sourcetmp)
        return result
        
        