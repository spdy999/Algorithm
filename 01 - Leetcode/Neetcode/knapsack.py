class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        subset = [0, 0] # [w, p]
        maxx = [0]

        def backtrack_dfs(i):
            if i >= len(weight):
                if subset[0] <= capacity: # check weight
                    maxx[0] = max(maxx[0], subset[1])
                return

            subset[0] += weight[i]
            subset[1] += profit[i]

            backtrack_dfs(i + 1) # left

            subset[0] -= weight[i]
            subset[1] -= profit[i]

            backtrack_dfs(i + 1) # right
        
        backtrack_dfs(0)
        return maxx[0]

# class Solution:
#     def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
#         subset = [[], 0, 0] # [[subset], w, p]
#         maxx = [0]

#         def dfs(i): # O(n^2)
#             if i >= len(weight): 
#                 if subset[1] <= capacity: # check weight
#                     maxx[0] = max(maxx[0], subset[2])
#                 return

#             subset[0].append(weight[i])
#             subset[1] += weight[i]
#             subset[2] += profit[i]
#             dfs(i + 1)
#             subset[0].remove(weight[i])
#             subset[1] -= weight[i]
#             subset[2] -= profit[i]
#             dfs(i + 1)
        
#         dfs(0)
#         return maxx[0]
