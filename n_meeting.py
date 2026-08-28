def n_meeting(start , end , m , count) -> int:
    i = 0
    end_max = end[0]
    while i < m:
        if start[i] > end_max:
            count += 1
            end_max = end[i]
        i += 1
    return count + 1
start = [ 0 , 3 , 1 , 6 , 7 , 11 , 16]
end = [6 , 5 , 2 , 8 , 10 , 15 , 18]
count = 0
m = len(start)
n = len(end)
print(n_meeting(start , end , m , count))
    