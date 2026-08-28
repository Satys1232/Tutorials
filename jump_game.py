def jump_poss(nums):
    max_index = 0
    for i in range(0 , len(nums)):
        if i > max_index:
            return False
        max_index = max(max_index , i + nums[i])
    return True

nums = [ 3 , 8 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
print(jump_poss(nums))