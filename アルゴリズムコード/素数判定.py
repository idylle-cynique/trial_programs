# シンプルな素数判定 O(√n)

def isprime(x):
    i = 2
    while(i**2 <= x):
        #print(x,":",i)
        if x%i == 0:
            return False       
        i += 1
    return True

# 動作確認用コード

n = 131071
print(isprime(n))
m = 13141
print(isprime(m))