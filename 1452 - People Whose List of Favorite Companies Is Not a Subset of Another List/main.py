from collections import defaultdict
class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        indexhashtableofcompany = defaultdict(set)
        result = []
        for index, parts in enumerate(favoriteCompanies):
            for company in parts:
                indexhashtableofcompany[company].add(index)
 
        
        for index, parts in enumerate(favoriteCompanies):
            subpart = indexhashtableofcompany[parts[0]]
            for company in parts[1:]:
                subpart = subpart & indexhashtableofcompany[company]
 
            if len(subpart) <= 1:
                result.append(index)
 
        return result
            
if __name__ == "__main__":
    source = [["kmccktodigztyrwpvlif","mcircxcauajyzlppedqy","rgjghlcicyocusukhmjb","zkcqvffyeekjdwqtjege"],
    ["kfkzsjhkdrtsztchhazh","kmccktodigztyrwpvlif","rgjghlcicyocusukhmjb"],
    ["kfkzsjhkdrtsztchhazh","kmccktodigztyrwpvlif","mcircxcauajyzlppedqy","zkcqvffyeekjdwqtjege"],
    ["kfkzsjhkdrtsztchhazh","kmccktodigztyrwpvlif","mcircxcauajyzlppedqy","rgjghlcicyocusukhmjb"],
    ["kfkzsjhkdrtsztchhazh","kmccktodigztyrwpvlif"]]
    result = Solution().peopleIndexes(source)
    print(result)
