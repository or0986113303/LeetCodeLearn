import collections
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        list1hash = {}
        list2hash = {}
        result = {}
        for index, parts in enumerate(list1):
            list1hash[parts] = index
        for index, parts in enumerate(list2):
            list2hash[parts] = index
            
        target = collections.Counter(list1) if len(list1) < len(list2) else collections.Counter(list2)
        sumresult = len(list1) + len(list2)
        for _,key in enumerate(target.keys()):
            print(key),
            if key in list1 and key in list2:
                result[list1hash[key] + list2hash[key]] = key
                if sumresult > list1hash[key] + list2hash[key]:
                    sumresult = list1hash[key] + list2hash[key]
        return result[sumresult]
                
if __name__ == '__main__':
    source1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    source2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    result = Solution().findRestaurant(source1, source2)
    print(result)