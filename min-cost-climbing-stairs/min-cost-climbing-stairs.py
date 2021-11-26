class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        mc = [0, 0]
        for i in range(2, len(cost)):
            mc.append(min(mc[-1] + cost[i - 1], mc[-2] + cost[i - 2]))
        return mc[-1]