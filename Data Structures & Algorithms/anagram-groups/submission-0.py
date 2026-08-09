class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in anagram:
                anagram[key]=[]
            anagram[key].append(word)
        return list(anagram.values())