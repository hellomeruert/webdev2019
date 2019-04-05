def big_diff(nums):
    minimum = nums[0]
    maximum = nums[0]

    for i in range(1, len(nums)):
        minimum = min(minimum, nums[i])
        maximum = max(maximum, nums[i])

    return maximum - minimum
