# gcd() - ユークリッドの互除法による二数の最大公約数の導出

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b) 

    
    
a,b = 368,216
a,b = int(a),int(b)

print(gcd(a,b))