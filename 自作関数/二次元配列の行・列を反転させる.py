# 正方形型・長方形型いずれの二次元配列でも回転可能

n_a = [[1,2,3],[4,5,6],[7,8,9]]     # 正方形型二次元リスト
n_b = [[0,".","="],[1,2,3],[4,5,6],[7,8,9]]  # 長方形型二次元リスト

def rotate_r(data_list):
    h,w = len(data_list),len(data_list[0])
    ans_list = []
    for i in range(w):
        temp = []
        for j in range(h):
            temp.append(data_list[j][i])
        ans_list.append(temp)
    
    return ans_list

def output_2dlist(data_list):
    for i in data_list:
        print(i)
    return print()

output_2dlist(n_a)
output_2dlist(rotate_r(n_a))

output_2dlist(n_b)
output_2dlist(rotate_r(n_b))