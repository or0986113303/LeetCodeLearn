# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recursioncount(self, source, hashmap):
        if not source:
            return
        
        if not source.val in hashmap:
            hashmap[source.val] = 1
        else :
            hashmap[source.val] += 2
        
        self.recursioncount(source.left, hashmap)
        self.recursioncount(source.right, hashmap)
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return 
        hashmap = {}
        self.recursioncount(root, hashmap)
        result = []
        mostcommon = 0
        for keys in hashmap:
            if hashmap[keys] > mostcommon:
                mostcommon = hashmap[keys]
        print(mostcommon)
        for keys in hashmap:
            if hashmap[keys] > mostcommon - 1 :
                result.append(keys)
        print(result)
        return result