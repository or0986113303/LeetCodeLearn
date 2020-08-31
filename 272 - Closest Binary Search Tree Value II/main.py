# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, source, target, result):
        if not source:
            return 
        if not source.val in result:
            result[source.val] = abs(target - source.val)
        self.dfs(source.left, target, result)
        self.dfs(source.right, target, result)
        
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        result = {}
        if not root.left and not root.right and root:
            return [root.val]
        elif not root.left and not root.right and not root:
            return [0]
        self.dfs(root, target, result)
        print(result)
        minimum = [float('inf'), None]
        for index, key in enumerate(result):
            if minimum[0] > result[key] :
                minimum[0] = result[key]
                minimum[1] = key
        sortedresult = sorted(result.items(), key=lambda items:items[1], reverse=False)
        print(sortedresult)
        arrresult = []
        for index in range(0, k, 1):
            arrresult.append(sortedresult[index][0])
        return arrresult
            