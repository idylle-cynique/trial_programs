def x_check(square):          # 斜めの並びのリストを作成
      hw = len(square)
      xs = []
      xs.append([square[i][i] for i in range(hw)])
      xs.append([square[hw-1-i][i] for i in range(hw-1,-1,-1)])
      return xs
      
def roco_check(square):       # 横・縦の並びのリストを作成
      hw = len(square)
      rows = [i for i in square]
      cols = [[square[i][j] for i in range(hw)] for j in range(hw)]
      return rows + cols

# 利用できるのは正方形型(行数と列数が等しい)二次元リストのみ
# 正方形型であれば長さは問わない

# サンプル
square = [[1,2,3],[4,5,6],[7,8,9]]

print("二次元リストサンプル")
for i in square:
    print(i)
print()
print("行と列のリスト")
for i in roco_check(square):
    print(i)
print()
print("斜めの並びのリスト")
for i in x_check(square):
    print(i)