import random

def insertion_sort(nums, reverse=False):
    for i in range(1,len(nums)):
        #print(nums[i],nums[:i+1])
        for j in range(i,0,-1):
            #print(":",nums[j-1],"<",nums[j],"?")
            if nums[j] < nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
            else:
                break
      
    if reverse == False:
        return nums
    else:
        return nums[::-1]

n = 30
nums = [random.randint(1,256) for x in range(n)]
nums = [ 27,  99, 218, 226,  98, 141, 124, 186, 155,  71,
        256,  11, 178, 196, 191,  92, 247, 122, 254, 123,
        215, 246,  29, 197,   7,  49, 206, 204, 118, 232]

print(nums)

print(insertion_sort(nums))
if insertion_sort(nums) == sorted(nums):
    print("insertion_sort: SUCCESS!")
else:
    print("Oops! this sorting program is somthing wrong... :(")