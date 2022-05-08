import random, collections

def isprime(x):
    i = 2
    while(i**2 <= x):
        #print(x,":",i)
        if x%i == 0:
            return False       
        i += 1
    return True
    
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

if __name__ == "__main__":

    n = random.randint(10**3,10**6)
    n = 10**6
    n_pfs = check_primefacts(n)
    n_cnt = collections.Counter(n_pfs)

    print(n_pfs)
    exit()
    output_primefacts(n_cnt)
