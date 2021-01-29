# 二分探索アルゴリズムコード

import random

def bin_search(nums,n):
      
      l,r = 0,len(nums)-1
      m = len(nums)//2
      print(nums); print(n,":",nums[m])
      if len(nums) == 1 and nums[0] != n:
            return False
      
      if nums[m] == n:
            return True
      elif nums[m] < n:
            return bin_search(nums[m+1:],n)
      else:
            return bin_search(nums[l:m] ,n)
      

n = 32
a =  sorted([770, 659, 765, 416, 901, 543, 655, 171, 981, 522, 677,
      386,  56, 782, 679, 470, 126, 649, 225, 991, 255, 121,
      194,  91, 565, 423, 763, 554, 666, 684, 739, 677])
#a = [random.randint(1,1000) for _ in range(n)] 
idx = random.randint(0,n-1)

print("Is there",a[idx],"in list-a?")

if bin_search(a,a[idx]) == True:
      print("-- Yes, there is!")
else:
      print("-- Sorry,",a[idx],"doesn't exist in this list...")