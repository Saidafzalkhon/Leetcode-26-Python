nums = list(map(int,input().split()))
list1 = set()
for i in nums:
    list1.add(i)
nums.clear()
for i in list1:
    nums.append(i)
nums.sort()
print(nums)