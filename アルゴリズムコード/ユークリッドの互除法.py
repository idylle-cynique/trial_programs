# gcd() - ユークリッドの互除法による二数の最大公約数の導出

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b) 

# 最大公約数を用いて最小公倍数も求めることができる
def lcm(gcdnum,a,b):
    return a*b // gcdnum
    
    
a,b = 368,216
gcdnum = gcd(a,b)
lcmnum = lcm(gcdnum,a,b)

print(gcdnum,lcmnum)