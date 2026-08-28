import math
def jump_game_ii(nums, index, jump):
    if index >= len(nums) - 1:
        return jump
    min_jump = math.inf
    for i in range(1, nums[index] + 1):
        min_jump = min(
            min_jump,
            jump_game_ii(nums, index + i, jump + 1)
        )
    return min_jump

nums = [2, 3, 1, 4, 1, 1, 1, 2]
print(jump_game_ii(nums, 0, 0))

