def maxminsum(arr):
    sum = 0
    for num in range(len(arr)):
        sum = sum + arr[num]
    print(sum - max(arr),sum - min(arr))





arr = [1,2,3,4,5]
maxminsum(arr)

