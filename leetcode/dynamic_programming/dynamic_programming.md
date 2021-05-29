+ [House Robber II](#house-robber-ii)
+ [House Robber](#house-robber)
<!-----solution----->

## House Robber

https://leetcode.com/problems/house-robber/

```python
def rob(self, nums: List[int]) -> int:  
    n = len(nums)
    if not n:
        return 0        
    memo = [None] * n
    
    def steal(n):
        if memo[n] != None:
            return memo[n]
        if n == 0:
            result = nums[0]
        elif n == 1:
            result = max(nums[0], nums[1])
        else:
            result = max(steal(n-1),  nums[n] + steal(n-2))
        memo[n] = result
        return result

    return steal(n-1)
```

## House Robber II

https://leetcode.com/problems/house-robber-ii/

```python
def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    
    if len(nums) <= 3:
        return max(nums)
    
    def helper(dp):
        dp[1] = max(dp[0], dp[1])

        for x in range(2, len(dp)):
            dp[x] = max(dp[x - 1], dp[x] + dp[x - 2])

        return dp[-1]
    
    p1 = helper(nums[:len(nums) - 1])
    p2 = helper(nums[1:])
    return max(p1, p2)
```
