# AtCoder Begginer Contest 091 - C問題のために作成したコード

# このコードではABC091-C問題をそのままシミュレートしている
# シミュレートをベースにした解の導出では計算量の問題で不正解(TLE)になってしまうが、
# 以下のコードに与える入力値(n,m)をいろいろな値を試すことで、シミュレートなしに解の導出が可能であるとわかる

def view_list(lst):　# 二次元リストを出力
    for i in lst:
        print(i)
    print()
    
    return True

n,m = map(int,input().split())
maps = [[0]*(n)]*m
h,w = len(maps),len(maps[0])

tmp_maps = [[-1]*(w+2)]
for i in maps:
    tmp_maps.append([-1] + i + [-1])
tmp_maps.append([-1]*(w+2))

#view_list(maps); view_list(tmp_maps)

maps = tmp_maps
dx = [-1, 0, 1,-1, 0, 1,-1, 0, 1]
dy = [-1,-1,-1, 0, 0, 0, 1, 1, 1]

for i in range(1,h+1):
    for j in range(1,w+1):
        #print(i,j)
        for k in range(len(dx)):
            if maps[i+dx[k]][j+dy[k]] != -1:
                if maps[i+dx[k]][j+dy[k]] == 0:
                    maps[i+dx[k]][j+dy[k]] = 1
                else:
                    maps[i+dx[k]][j+dy[k]] = 0
            
        view_list(maps); print()

view_list(maps)