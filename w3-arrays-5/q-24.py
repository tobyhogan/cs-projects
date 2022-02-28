nums = [1, 3, 5, 8, 9, 2, 5, 3, 7, 7]

for num in nums:
    if nums.count(num) > 1:
        nums.remove(num)

print(nums)
