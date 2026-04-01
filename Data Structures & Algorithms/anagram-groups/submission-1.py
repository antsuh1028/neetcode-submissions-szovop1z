class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(str1, str2):
            if len(str1) != len(str2):
                return False
            else:
                return sorted(str1) == sorted(str2)
        
        final = []
        dct = {}

        for i in range(len(strs)):
            string1 = strs[i]
            temp = [string1]
            for j in range(len(strs)):
                string2 = strs[j]
                if i == j:
                    continue
                if isAnagram(string1, string2):
                    temp.append(string2)
            if sorted(temp) not in final:
                final.append(sorted(temp))

        return final