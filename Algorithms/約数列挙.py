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



if __name__ == "__main__":
    n = 311
    nums = check_divs(n)

    print(nums)
