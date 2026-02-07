class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        for i in strs:
            k = "".join(sorted(i))
            anagram[k].append(i)
        return list(anagram.values())


        