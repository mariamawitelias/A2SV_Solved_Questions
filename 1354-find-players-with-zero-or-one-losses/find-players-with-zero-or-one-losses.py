class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # answer0 = set()
        # answer1 = []
        # lose = {} 
        # for winner, loser in matches:
        #     lose[loser] = lose.get(loser, 0) + 1
        # for key, value in lose.items():
        #     if value == 1:
        #         answer1.append(key)
        # for winner in matches:
        #     if winner not in lose:
        #         answer0.add(winner)    
        # ans = list(answer0)
        # ans.sort()
        # answer1.sort()
        # return [ans, answer1]
        answer0, answer1 = [], []
        lose = {}
        for winner, loser in matches:
            lose[loser] = lose.get(loser, 0) + 1
            lose[winner] = lose.get(winner, 0)
        for key, value in lose.items():
            if value == 0:
                answer0.append(key)
            if value == 1:
                answer1.append(key)
        answer0.sort()
        answer1.sort()
        return [answer0, answer1]
                


        
        