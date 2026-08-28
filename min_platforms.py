arr = [900 , 840 , 950 , 1100 , 1500 , 1800]
dep = [910 , 1200 , 1120 , 1130 , 1900 , 2000]
max_platforms = 0
for i in range(len(arr)):
    platform_needed_now = 0
    for j in range(len(arr)):
        if arr[j] <= arr[i] <= dep[j]:
            platform_needed_now += 1
    max_platforms = max(max_platforms , platform_needed_now)
print(max_platforms)