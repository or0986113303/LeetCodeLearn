# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfsmakenumbers(self, rootval, source, prevpath, isfirst, allofnumbers):
        if not source:
            return
        elif not source.left and not source.right:
            if isfirst:
                prevpath = rootval
                prevpath = prevpath + str(source.val)
                isfirst = False
                allofnumbers.append(prevpath)
            else:
                prevpath = prevpath + str(source.val)
                allofnumbers.append(prevpath)
            return
        if isfirst:
            prevpath = rootval
            isfirst = False
        self.dfsmakenumbers(rootval, source.left, prevpath + str(source.val), isfirst, allofnumbers)
        self.dfsmakenumbers(rootval, source.right, prevpath + str(source.val), isfirst, allofnumbers)
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left and not root.right:
            return root.val
        allofnumbers = []
        prevpath = ''
        self.dfsmakenumbers(str(root.val), root.left, prevpath, True, allofnumbers)
        self.dfsmakenumbers(str(root.val), root.right, prevpath, True, allofnumbers)
        print(allofnumbers)
        sumofall = 0
        for part in allofnumbers:
            sumofall += int(part)
        return sumofall
        