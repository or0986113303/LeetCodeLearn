"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def recursionofsubordinates(self, source, result, infohash):
        result[0] += infohash[source][0]
        for part in infohash[source][1] :
            self.recursionofsubordinates(part, result, infohash)
            
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        infohash = {}
        for part in employees:
            if part.id not in infohash:
                infohash[part.id] = [part.importance, part.subordinates]
        result = [0]
        for _, key in enumerate(infohash):
            if key == id :
                self.recursionofsubordinates(key, result, infohash)
        return result[0]
                