import random

def bubble_sort(nums,reverse=False):
    for i in range(len(nums)-1):
        print("{:2}".format(i+1),nums)
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    
    if reverse == False:
        return nums
    else:
        return nums[::-1]

n = 30
nums = [random.randint(1,256) for x in range(n)]
#nums = [304, 739, 242, 83, 723, 36, 967, 763, 66, 124,
#        402,860, 567, 271, 483, 721, 977, 128, 448, 215, 288,
#        1,648, 883, 96, 18, 815, 848, 441, 188]
        
print(nums)

if sorted(nums) == bubble_sort(nums):
    print("bubble_sort: SUCCESS!")
else:
    print("Oops!... This sort function is something wrong... :(")