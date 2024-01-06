#1235. Maximum Profit in Job Scheduling

#We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
#You're given the startTime, endTime and profit arrays, 
#return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
#If you choose a job that ends at time X you will be able to start another job that starts at time X.


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        number_of_jobs = len(profit)
        dp = [0] * (number_of_jobs + 1)
        for i, (current_end_time, current_start_time, current_profit) in enumerate(jobs):
            index = bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[index] + current_profit)
        return dp[number_of_jobs]
