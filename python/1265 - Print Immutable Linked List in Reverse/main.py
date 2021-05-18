class Solution(object):
    def printLinkedListInReverse(self, head):
        """
        :type head: ImmutableListNode
        :rtype: None
        """
        if not head:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()