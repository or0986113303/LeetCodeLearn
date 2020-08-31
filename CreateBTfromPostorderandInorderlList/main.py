class Node(object):
    def __init__(self, key = None, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

class Solution(object):
    def createNode(self, postorder, inorder, start, end, index):
        if start >= end:
            return None
        node = Node(postorder[index[0]])  
        index[0] -= 1
        if start == end:
            return None
        
        operatorindex = self.searchindex(inorder, start, end, node.key)

        node.left = self.createNode(postorder, inorder, operatorindex + 1, end, index)
        node.right = self.createNode(postorder, inorder, start, operatorindex - 1, index)
        return node
    
    def searchindex(self, inorder, start, end, value):
        index = 0
        for index in range(start, end + 1, 1):
            if inorder[index] == value:
                return index
        return index

    def createTree(self, postorder, inorder, length):
        index = [length - 1] 
        return self.createNode(postorder, inorder, 0, length - 1, index)

    def inordertraversal(self, source):
        if source is None:
            return
        print(source.key)
        self.inordertraversal(source.left)
        
        self.inordertraversal(source.right)

if __name__ == "__main__":
    postorder = [8, 4, 5, 2, 6, 7, 3, 1]
    inorder = [4, 8, 2, 5, 1, 6, 3, 7]
    length = len(postorder)
    tree = Solution().createTree(postorder, inorder, length)
    Solution().inordertraversal(tree)