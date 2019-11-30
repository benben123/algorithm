class Solution:
    def setAnagram(self, strs):
        import collections
        anagram_map, result = collections.defaultdict(list), []
        for s in strs:
            sorted_s = ("").join(sorted(s))
            anagram_map[sorted_s].append(s)
        for anagram in anagram_map.values():
            anagram.sort()
            result.append(anagram)
        return result


if __name__ == "__main__":
    result = Solution().setAnagram(["cat", "def", "act", "fed"])
    print result
