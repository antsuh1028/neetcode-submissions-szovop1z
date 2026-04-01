class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        dct = defaultdict(list)
        for string in strs:
            sortedS = ''.join(sorted(string))
            dct[sortedS].append(string)
        for value in dct.values():
            final.append(value)
        return final