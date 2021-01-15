# エラトステネスのふるい
def elatos(n):
      x = 2
      shieve = set([int(x) for x in range(2,n+1)])
      garbage = set()
      check_list = set()

      while(x*x < n):
            garbage = set([x*int(i)+x for i in range(1,n//x+1)])
            shieve -= garbage
            check_list.add(x)
      
            #print(shieve)
            #print(min(shieve-check_list))
      
            x = min(shieve-check_list)
      
      return shieve

n = 10**6
ela_set = elatos(n)
print(ela_set)

n = int(input())
