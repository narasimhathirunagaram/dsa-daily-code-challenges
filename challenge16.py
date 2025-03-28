# https://leetcode.com/problems/coin-change/description/

# Coin Change:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        least_val = min(coins)
        if amount<least_val:
            return 0
        cnt = 0
        coins.sort(reverse=True)
        for i in coins:
            print(amount,i,cnt)
            if amount>=i:
                cnt += amount//i
                amount = amount%i
            
        if amount == 0:
            return cnt
        else:
            return -1
            

        

if __name__ == '__main__':
    # coins1, amount1 = [1,2,5], 11
    # coins2, amount2 = [2], 3
    # coins3, amount3 = [1], 0
    coins4, amount4 = [186,419,83,408], 6249
    sol = Solution()
    # print(sol.coinChange(coins1,amount1))
    # print(sol.coinChange(coins2,amount2))
    # print(sol.coinChange(coins3,amount3))
    print(sol.coinChange(coins4,amount4))
