def multiply(arr,num):
    for index, x in enumerate(arr):
        print x, num
        arr[index] = x * num
        print arr
    return arr


a = [2,4,10,16]
b = multiply(a,5)
print b