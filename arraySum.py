
def simpleArraySum(arr):
    arrSum = 0
    for i in range(len(arr)):
        arrSum+=arr[i]
        i+=1
    return arrSum



arr2= [1,2,3,4,5]
print(simpleArraySum(arr2))

