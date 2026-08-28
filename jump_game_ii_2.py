l = 0
r = 0 
nums = [ 2 , 3 , 1 , 4 , 1 , 1 , 1 , 2 ]
jump = 0
n = len(nums)
while r < n-1:
    farthest = 0
    for i in range(l , r+1):
        farthest = max(farthest , i + nums[i])
    l = r + 1
    r = farthest
    jump += 1
    

    