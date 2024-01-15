#2225. Find Players With Zero or One Losses


#You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.
#Return a list answer of size 2 where:
#answer[0] is a list of all players that have not lost any matches.
#answer[1] is a list of all players that have lost exactly one match.
#The values in the two lists should be returned in increasing order.
#Note:
#You should only consider the players that have played at least one match.
#The testcases will be generated such that no two matches will have the same outcome.

#1st code (124/127 test cases passed)
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners =[]
        losers=[]

        for i in matches:
            winners.append(i[0])
            losers.append(i[1])

        set_win=set(winners)
        set_loss=set(losers)
        total_players=(set_win|set_loss)

        res1=list(total_players-set_loss)
        res2=[]

        for i in total_players:
            if losers.count(i)==1:
                res2.append(i)

        ans=[sorted(res1),sorted(res2)]
        return ans

#optimized code:-
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count_dict = {}
        unique_winners = set()
        unique_losers = set()

        for match in matches:
            winner, loser = match
            unique_winners.add(winner)
            unique_losers.add(loser)
            count_dict[loser] = count_dict.get(loser, 0) + 1

        res1 = list(unique_winners - unique_losers)
        res2 = [player for player, count in count_dict.items() if count == 1]

        ans = [sorted(res1), sorted(res2)]
        return ans
