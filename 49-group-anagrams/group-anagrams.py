class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        signatures = defaultdict(list)

        for word in strs:
            signatures["".join(sorted(word))].append(word)

        return list(signatures.values())