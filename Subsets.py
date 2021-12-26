def subsets(nums):

    res = []

    def dfs(nums, path, res):

        res.append(path)

        for i in range(len(nums)):
            dfs(nums[i+1:], path+[nums[i]], res)

    dfs(nums, [], res)

    print(res)

subsets([1,2,3])