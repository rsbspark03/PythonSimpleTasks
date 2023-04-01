
nums = [2,3,4,1,5]
target = 5
i = 0
j = 1
ans = []
while i < len(nums):
    #print(i)
    #print(j)
    while j < len(nums):
        #print(i)
        #print(j)
        if (nums[i] + nums[j]) == target:
            ans.append(i)
            ans.append(j)
        j += 1
    i += 1
    j = i + 1

ans = set(ans)
ans = tuple(ans)
ans = list(ans)
print(ans)
    