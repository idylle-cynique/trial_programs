def calc_nCr(n,r):
    r = min(n-r,r)
    numer = 1
    denom = 1
    for i in range(n,r,-1):
        numer *= i
        denom *= (n-i+1)
    #print(numer,"/",denom)
    return numer//denom