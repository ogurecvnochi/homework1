nums = [1, 2, 3, 4, 5, 6, 4]
target = 7
res = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target and sorted((nums[i], nums[j])) not in res:
            print((nums[i], nums[j]))
            res.append(sorted((nums[i], nums[j])))