### Step 1: Count the number of times an integer occurs in arr
### Step 2: Divide the number count by 2
### return the sum of pairs

from collections import Counter
def sockMerchant(n, ar):
    sockes_count = Counter(ar)
    pair_dict=sockes_count.values()  ### [4,3,1,1]
    return sum(i//2 for i in pair_dict)  ### divide each by 2 and return the sum


arr=[10, 20, 20, 10, 10, 30 ,50 ,10, 20]
print('Total Number of Pairs: ',sockMerchant(9, arr))
