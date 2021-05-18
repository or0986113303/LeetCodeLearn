class Node(object):
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Solution(object):
    def createNode(self, source, index, created, result):
        if created[index] is not None:
            return
        created[index] = Node(index)

        if source[index] == -1 :
            result[0] = created[index]
            return
        
        if created[source[index]] is not None:
            self.createNode(source, source[index], created, result)
        
        tmp = created[source[index]]

        if tmp.left is None:
            tmp.left = created[index]
        elif tmp.right is None:
            tmp.right = created[index]


    def createTree(self, source):
        length = len(source)
        result = [None]
        created = [None]*(length + 1)
        for index in range(length):
            self.createNode(source, index, created, result)
        return result[0]

    def inorderTraversal(self, source):
        if source is not None:
            self.inorderTraversal(source.left)
            print(source.key)
            self.inorderTraversal(source.right)

if __name__ == "__main__":
    source = [-1, 0, 0, 1, 1, 3, 5] 
    tree = Solution().createTree(source)
    Solution().inorderTraversal(tree)