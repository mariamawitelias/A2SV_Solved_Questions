class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        # for i in strs:
        #     k = "".join(sorted(i))
        #     anagram[k].append(i)
        # return list(anagram.values())
        
        for i in strs:
            count = Counter(i)
            k = tuple(sorted(count.items()))
            anagram[k].append(i)
        return list(anagram.values())

        