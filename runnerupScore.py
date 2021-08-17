
## length of list
n=int(input())

### taking list as input
arr=list(map(int, input().split()))[:n]


### store max value of list in max_elem
max_elem=max(arr)


### loop until all the max numbers are removed and return the second max number
while max(arr)==max_elem:
    arr.remove(max(arr))
print(max(arr))
