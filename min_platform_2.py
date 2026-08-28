arr = [900 , 940 , 950 , 1100 , 1500 , 1800]
dep = [910 , 1120 , 1130 , 1200 , 1900 , 2000]
ans = 1
count = 1
arr.sort()
dep.sort()
n = len(arr)
i = 1
j = 0
while i < n and j < n:
    if arr[i] <= dep[j]:
        count += 1
        i += 1
    else:
        count -=1
        j += 1
    ans = max(ans , count)
print(ans)