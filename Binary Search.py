s = [1, 2, 3, 4]

def bin_search(nums, target):

    l, r = 0, len(nums)-1

    while l < r:

        mid = (l + r) // 2

        if nums[mid] == target:
            l = mid
            break
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return l

out = bin_search(s, 4)
print(s[out])