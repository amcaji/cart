def knapsack(values, weights, W):
    n = len(values)
    dp= [[0]*(W+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        for w in range(1,W+1):
            if weights[i-1] <= w:
                dp[i][w]=max(values[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[n][W]
        
        

n=int(input("Enter Number of items: "))

values=list(map(int,input("Enter the values on this same line: ").split()))
weights=list(map(int,input("Enter the weights on this same line: ").split()))
W = int(input("Enter the max weight capacity for the knapsack"))


print("Maximum value in knapsack = ",knapsack(values , weights, W))