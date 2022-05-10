# エラトステネスのふるい

'''
      素数そのものをリストに格納するのではなく、 指定した数値分だけの長さのリストを用意し、
      値として素数かそうでないかを示す論理値を格納するようにする

      2から順にループを開始し、その値の倍数に非素数判定を与えていく
      またこの時の非素数判定に際して
      素数でないことが分かっている数の倍数の非素数判定は
      その素数の素因数の倍数の非素数判定処理で既に完了しているので二度同じ処理はせずパスする

      最後にふるいリストの中から素数判定されているものだけをループで抜き出したものを返す
      これによって集合演算を行うことなく昇順ソート済みの素数リストをこれまでよりも断然高速に得ることができる
      高速化の幅はどれくらいの大きさの値までの素数を求めるのかにも左右されるが、N = 1000000であれば
      素数リストを得るのにかかる時間はおおむね10倍高速化され、Nの値が大きくなればなるほど高速化される
'''

# 新しいエラトステネスのふるい
def elatos(number):
      shieve = [True for x in range(number+1)]
      shieve[0] = False; shieve[1] = False

      n = 2
      while(n**2 < number):
            if shieve[n]:
                  for x in range(2,number//n+1):
                        shieve[n*x] = False
            n += 1

      primes = list()
      for i,v in enumerate(shieve):
            if v:
                  #print(i,v)
                  primes.append(i)
      return primes

# 過去に用いていた古いエラトステネスのふるい
def primitive_elatos(n): 
      x = 2
      shieve = set([int(x) for x in range(2,n+1)])
      garbage = set()
      check_list = set()

      while(x*x < n):
            garbage = set([x*int(i)+x for i in range(1,n//x+1)])
            shieve -= garbage
            check_list.add(x)
            x = min(shieve-check_list)
      return shieve




if __name__ == "__main__":
      import time
      n = 10**6
      start = time.time()
      ela_set = elatos(n)
      end = time.time()
      print(f"new_elatos:{len(ela_set)}, process_time:{end-start}")

      start = time.time()
      priela_set = primitive_elatos(n)
      end = time.time()
      print(f"old_elatos:{len(priela_set)}, process_time:{end-start}")

      

      #print(ela_set)