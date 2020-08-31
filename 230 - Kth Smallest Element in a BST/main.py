class Solution(object):
    def inorder(self, source, result):
        if not source :
            return
        self.inorder(source.left, result)
        result.append(source.val)
        self.inorder(source.right, result)
    def kthSmallest(self, root, k):
        if not root:
            return 
        result = []
        self.inorder(root, result)
        return result[k - 1]

if __name__ == "__main__":
    print('hello world')