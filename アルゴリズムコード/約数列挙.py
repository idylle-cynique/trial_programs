# 約数の高速列挙
def check_divs(n):
    x = 1
    
    lower_divs = []
    greater_divs = []
    while(x*x <= n):
        if n%x == 0:
            lower_divs.append(x)
            if x**2 != n:     
                greater_divs.append(n//x)
        x += 1
    
    divnums = lower_divs + greater_divs[::-1]
    return divnums

n = 720
nums = chk_divisors(n)

print(nums)
