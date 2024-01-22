#645. Set Mismatch

#You have a set of integers s, which originally contains all the numbers from 1 to n. 
#Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#You are given an integer array nums representing the data status of this set after the error.
#Find the number that occurs twice and the number that is missing and return them in the form of an array.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums1 = [i for i in range(1, len(nums) + 1)]
        a1 = set([i for i in nums if nums.count(i) == 2])
        ans = list(a1)
        ans.append(sum(nums1) - sum(set(nums)))
        return ans 
