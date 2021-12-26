def removeDuplicates(nums):

    redict = set()
    out = []
    
    for i in nums:
        if i not in redict:
            redict.add(i)
            out.append(i)
            
    return len(redict), out

nums = [1,1,2]
k, out = removeDuplicates(nums)
print(k, out)