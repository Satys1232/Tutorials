def lemonade() :
    mydict = {}
    mydict[5] = 0
    nums = [10]
    n = len(nums)
    for i in range(0 , n):
        x = 0
        if nums[i] == 5:
            mydict[nums[i]] = mydict.get(nums[i] , 0) + 1
        if nums[i] > 5 :
           x = nums[i] / 5
           if mydict[5] < x-1 :
                return False 
    return True

print(lemonade())