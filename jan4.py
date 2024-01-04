#2870. Minimum Number of Operations to Make Array Empty

#You are given a 0-indexed array nums consisting of positive integers.
#There are two types of operations that you can apply on the array any number of times:
#Choose two elements with equal values and delete them from the array.
#Choose three elements with equal values and delete them from the array.
#Return the minimum number of operations required to make the array empty, or -1 if it is not possible.


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = {}
        result = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for count in counts.values():
            if count == 1:
                return -1
            if count % 3 == 1:
                result += (count // 3) - 1
                result += 2
            else:
                result += count // 3
                result += (count % 3) // 2
        return result
