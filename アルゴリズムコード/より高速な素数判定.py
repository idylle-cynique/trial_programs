# より高速な素数判定 O(√n)

# 2以外の偶数が素数でないことは既に明らかなので、
# ループは i=3 から始めて2ずつインクリメントしていけば、ある数に至るまでのループ回数が1/2になる

def isprime(x):
    if x == 2:
        return True
    
    i = 3
    while(i**2 <= x):
        #print(x,":",i)
        if x%i == 0:
            return False       
        i += 2
    return True

# 動作確認用コード

n = 131071
print(isprime(n))
m = 13141
print(isprime(m))