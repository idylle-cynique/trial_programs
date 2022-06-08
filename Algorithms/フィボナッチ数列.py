# 基本的なフィボナッチ数列の得方
N = 40 

def fibonacci(n):
    fibo_nums = [0,1]
    nums = 0
    for i in range(1,n):
        nums = fibo_nums[-2] + fibo_nums[-1]
        fibo_nums.append(nums)
        print(nums)
    
    return fibo_nums[-1]

print(fibonacci(N))