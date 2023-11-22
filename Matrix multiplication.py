a = [[1, 6], [2, 3]]
b = [[7, 9, 3], [12, 6, 1], [8, 4, 5]]

if len(a[0]) == len(b):
    print("Can proceed further steps")
    arr = []
    for i in range(len(a)):
        arr.append(([0] * len(b[0])))
    print(arr)
    
    for i in range(len(a)):
        sum = 0
        j = 0
        k = 0
        while j < len(b[0]):
            sum += (a[i][k] * b[k][j])
            k += 1
            if k == len(b):
                arr[i][j] = sum
                sum = 0
                j += 1
                k = 0
                
    print(arr)            
else:
    print("Can't proceed")
