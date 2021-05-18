"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution(object):
    accessedhashtable = {}
    def dfs(self, source):
        if not source:
            return None
        elif source in self.accessedhashtable:
            return self.accessedhashtable[source]
        
        result = Node(x=source.val)
        
        self.accessedhashtable[source] = result
        result.next = self.dfs(source.next)
        result.random = self.dfs(source.random)
        return result
        
        
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        elif head in self.accessedhashtable:
            return self.accessedhashtable[head]
        
        result = Node(x=head.val)
        
        self.accessedhashtable[head] = result
        result.next = self.dfs(head.next)
        result.random = self.dfs(head.random)
        return result