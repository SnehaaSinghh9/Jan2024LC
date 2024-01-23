#1239. Maximum Length of a Concatenated String with Unique Characters

#You are given an array of strings arr. 
#A string s is formed by the concatenation of a subsequence of arr that has unique characters.
#Return the maximum possible length of s.
#A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = [0]
        self.dfs(arr, "", 0, result)
        return result[0]

    def dfs(self, arr, path, idx, result):
        if self.isUniqueChars(path):
            result[0] = max(result[0], len(path))

        if idx == len(arr) or not self.isUniqueChars(path):
            return

        for i in range(idx, len(arr)):
            self.dfs(arr, path + arr[i], i + 1, result)

    def isUniqueChars(self, s):
        char_set = set()
        for c in s:
            if c in char_set:
                return False
            char_set.add(c)
        return True
