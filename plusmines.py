def plusminus(arr):
    a = len(arr)
    n = 0
    p = 0
    z = 0
    for i in arr:
        if i < 0:
            n +=1
        elif i > 0:
            p += 1
        else:
            z +=1
    print(format(float(p / a), '.6f')) 
    print(format(float(n / a), '.6f'))
    print(format(float(z / a), '.6f'))   
    return format(float(p / a), '.6f'), format(float(n / a), '.6f'),format(float(z / a), '.6f')
    

arr = [-4, 3, -9, 0, 4, 1]
plusminus(arr)