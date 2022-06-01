#N,M = map(int,input().split())
#coins = [int(x) for x in input().split()]

def view_dp(array):
    for row in array:
        print(row)
    return True

N,M = 15,6
Coins = [0,1,2,7,8,12,50]
dp = []

for j in range(M+1): # DPテーブルには初期値としてINFを与えておく
    dp.append([float('INF')] * (N+1))

for i in range(M+1): # 0円を払うのに必要なコインの枚数は常に0
    dp[i][0] = 0

#view_dp(dp)

for i in range(1,M+1):
    for j in range(1,N+1):
        #print(i,"枚目までのコインを使って",j,"円を作る"); print(i,"枚目までのコインは",Coins[:i]); print()
        
        if j < Coins[i]: # i枚目のコインの値が払いたい金額よりも大きいとき
            # i枚目のコインを使う余地はないので、 i-1枚目までのコインだけを用いて支払えばよい
            dp[i][j] = dp[i-1][j] 
        else:            # そうでないとき
            # (1) i枚目までのコインを使って支払うときの最小枚数か、
            # (2) i枚目までのコインを使ってj-c[i]円まで支払った時の最小枚数+1枚
            # のうち、より使用枚数が少ない方が所要最小枚数だと言える
            dp[i][j] = min(dp[i-1][j], dp[i][j-Coins[i]]+1)

view_dp(dp)

print(dp[M][N])

