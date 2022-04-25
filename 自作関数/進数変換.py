
def BaseKtoBase10(Number,K): # Base進数で記述された文字列数字を整数型の十進数に変換する
    Nums = list(Number)
    length = len(Nums)
    ret = 0
    
    for i in range(length):
        ele = int(Nums.pop())
        ret += ele * (K**i)
    
    return ret

def Base10toBaseK(Number,K): # 10進数で記述された数字をK進数に変換し、文字列で返す
    if 10 < K: # この関数では一桁進数以外は処理できないのでFalseを返す
        return False

    ret = []
    while(Number//K):
        ret.append(str(Number%K))
        Number //= K
    
    ret.append(str(Number))
    ret.reverse()

    return "".join(ret)
 
def exBase10toBaseK(Number,K): # Base10toBaseK()の拡張版。最大で35進数にまで変換が可能
    if 35 < K: # この関数では35進数以上には処理できないのでFalseを返す
        return False
    
    NumDict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',5: '5', 6: '6', 7: '7', 8: '8', 
               9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 
               18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q',
               27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}  

    ret = []
    while(Number//K):
        ret.append(str(NumDict[Number%K]))
        Number //= K
    
    ret.append(str(NumDict[Number]))
    ret.reverse()

    return "".join(ret)    


if __name__ == '__main__':
    # 10進数の255を3進数で表現する
    N = 255
    K = 3
    Answer = Base10toBaseK(N,K)
    print("10進数である{}を{}進数に直すと{}となる".format(N,K,Answer))
    print(type(Answer),":",Answer)

    # 10進数の65535を12進数で表現する
    M = 65535
    L = 12
    Answer = exBase10toBaseK(M,L)
    print("10進数である{}を{}進数に直すと{}となる".format(M,L,Answer))
    print(type(Answer),":",Answer)
