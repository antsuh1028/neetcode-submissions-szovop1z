class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dct = {}

        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1
            if tuple(count) in dct:
                dct[tuple(count)].append(string)
            else:
                dct[tuple(count)] = [string]
        print()
        return list(dct.values())
            

