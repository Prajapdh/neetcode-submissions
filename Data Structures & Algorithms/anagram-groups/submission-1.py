class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for s in strs:
            m=[0]*26
            for c in s:
                m[ord(c)-ord('a')]+=1
            anagrams[tuple(m)].append(s)
        
        return anagrams.values()