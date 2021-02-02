import random 

def selection_sort(nums,reverse=False):
    for i in range(len(nums)):
        print(nums)
        min_i = i
            
        for j in range(i+1,len(nums)):
            if nums[min_i] > nums[j]:
                min_i = j
        nums[i],nums[min_i] = nums[min_i],nums[i]
      
    if reverse == False:
        return nums
    else:
        return nums[::-1]

n = 30
nums = [random.randint(1,256) for x in range(n)]
nums = [3, 161, 173, 136, 46, 124, 37, 253, 146, 79, 68,
        38, 125, 157, 162, 190, 102, 158, 31, 48, 65, 194,
        252, 30, 100, 43, 46, 81, 36, 44]

print(nums)
print(selection_sort(nums))

if sorted(nums) == selection_sort(nums):
    print("selection_sort: SUCCESS!")