s = [1, 2, 3, 4, 5]

def bin_search(nums, target):

    l, r = 0, len(nums)

    while l < r:

        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1


def searchRange(nums, target):

    def searchFirst(x):
            
            l, r = 0, len(nums)
            
            while l < r:
                
                m = (l + r) // 2
                
                if nums[m] >= x:
                    
                    r = m
                    
                else:
                    
                    l = m + 1
    
            return l
        
    start = searchFirst(target)
    end = searchFirst(target+1)-1

    print(start, end)
        
    if start <= end: return [start, end]
    
    return [-1, -1]

nums = [5,7,7,8,8,10]
target = 1

# res = searchRange(nums, target)
res = bin_search(s, target)
print(res)