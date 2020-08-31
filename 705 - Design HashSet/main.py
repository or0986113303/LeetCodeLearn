class node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class Bucket(object):
    def __init__(self):
        self.source = node(value=0)
        
    def insert(self,value):
        if not self.isvalueexist(value):
            newtmp = node(value=value, next=self.source.next)
            self.source.next = newtmp
            
    def delete(self, value):
        prev = self.source
        curr = self.source.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            
    def __resursivetraversal__(self, source, value):
        if not source:
            return False
        if source.value == value:
            return True
        else :
            return self.__resursivetraversal__(source.next, value)
        
    def isvalueexist(self, value):
        operator = self.source.next
        return self.__resursivetraversal__(operator, value)
        
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 1024
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
    
    def __hash__(self, key):
        return key % self.keyRange
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self.__hash__(key)
        self.bucketArray[bucketIndex].insert(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self.__hash__(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self.__hash__(key)
        return self.bucketArray[bucketIndex].isvalueexist(key)

if __name__ == '__main__':
    obj = MyHashSet()
    obj.add(1)
    result = obj.contains(1)
    print(result)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)