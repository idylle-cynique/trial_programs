def check_primefacts(n): # 素因数を求める
    x = 2
    prime_factors = []

    while(x*x <= n):
        if n%x == 0:
            #print(n,x); print(":",prime_factors)
            prime_factors.append(x)
            n //= x
            x = 2
        else:
            x += 1
    
    prime_factors.append(n)
    return prime_factors

def output_primefacts(pfs_lst): # 素因数リストを式として出力
    outputs = []
    for i in n_cnt: 
        #print(i,n_cnt[i])
        outputs.append((str(i),"^",str(n_cnt[i])))

    for i in range(len(outputs)):
        print("".join(outputs[i]),end="")
        
        if i+1 != len(outputs):
            print(" + ",end="")
        else:
            print(" =",n)
    
    return True

import random, collections

n = random.randint(10**3,10**6)
n_pfs = check_primefacts(n)
n_cnt = collections.Counter(n_pfs)

output_primefacts(n_cnt)
