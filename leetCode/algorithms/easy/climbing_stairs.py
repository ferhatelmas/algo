class Solution:
    cache = {}

    def climbStairs(self, n):
        if n <= 2:
            return n
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n - 1)
        if n > 1:
            self.cache[n] += self.climbStairs(n - 2)
        return self.cache[n]
    //the cpp solution
    class Solution {
public:
    int climbStairs(int n) {
      long int dp[n+1];
        dp[0]=1,dp[1]=2;
        if(n<=2) return n;
        for(int i=2;i<=n;i++)
        {
            dp[i]=dp[i-1]+dp[i-2];
        }
        return dp[n-1];
    }
};
