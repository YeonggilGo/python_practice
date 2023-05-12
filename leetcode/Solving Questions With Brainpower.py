# https://leetcode.com/problems/solving-questions-with-brainpower/description/
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            point = questions[i][0]
            jump = questions[i][1]

            next_question = min(n, i+jump+1)
            dp[i] = max(dp[i+1], point + dp[next_question])
        return dp[0]


questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
s = Solution()
print(s.mostPoints(questions))
