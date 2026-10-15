class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1

            clave=tuple(counts)
            grupos[clave].append(word)

        return list(grupos.values())