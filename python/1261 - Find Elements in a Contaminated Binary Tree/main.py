# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.__result__ = [[]]
        self.__caculatetpye__ = {'left':self.__leftconvert__, 'right':self.__rightconvert__, 'root':self.__rootconvert__}
        self.__makearrayfromsource__(root, 0, self.__result__, 'root', 0)
    
    def __rootconvert__(self, node, prevvalue):
        return 0
    
    def __leftconvert__(self, node, prevvalue):
        return 2 * prevvalue + 1
    
    def __rightconvert__(self, node, prevvalue):
        return 2 * prevvalue + 2
        
    def __makearrayfromsource__(self, source, level, result, subtreetype, prevvalue):
        if not source:
            return
        if len(result) - 1 >= level:
            result[level].append(self.__caculatetpye__[subtreetype](source, prevvalue))
            source.val = self.__caculatetpye__[subtreetype](source, prevvalue)
        else :
            result.append([self.__caculatetpye__[subtreetype](source, prevvalue)])
            source.val = self.__caculatetpye__[subtreetype](source, prevvalue)
        
        self.__makearrayfromsource__(source.left, level + 1, result, 'left', source.val)
        self.__makearrayfromsource__(source.right, level + 1, result, 'right', source.val)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        result = False
        for index, part in enumerate(self.__result__):
            result = result or target in part
        return result
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)