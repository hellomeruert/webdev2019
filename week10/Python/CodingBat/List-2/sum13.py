def sum13(nums):
    s = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 1
        else:
            s += nums[i]

        i += 1

    return s