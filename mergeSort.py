

# Consider two sorted arrays
sorted_arr1 = [ 2, 4, 6, 8, 10, 12 ]
sorted_arr2 = [ 3, 5, 7, 9, 11, 13 ]


# consider an unsorted array
# unsorted_arr = [9,4,6,2,4,8,1]


def mergeSort(unsorted_arr):
    if len(unsorted_arr) <= 1:
        return unsorted_arr

    middle = len(unsorted_arr)//2  # [2]

    # starting from 0 till middle element
    left = unsorted_arr[:middle]

    # starting from middle to end of arra
    right = unsorted_arr[middle:]

    # (recursion) this will return sorted left and right arrays
    left = mergeSort(left)
    right = mergeSort(right)

    # return the final sorted array
    return merged_sorted_array(left,right)




# to merge two sorted arrays and return a single sorted array
def merged_sorted_array(sorted_arr1, sorted_arr2):

    # final sorted list
    sorted_list=[]

    # specifying lengths of both sorted arrays
    len_arr1 = len(sorted_arr1)
    len_arr2 = len(sorted_arr2)

    # starting from first element
    i = j = 0

    # iterate through each element and compare elements
    while i < len_arr1 and j < len_arr2:

        if sorted_arr1[ i ] < sorted_arr2[ j ]:
            sorted_list.append(sorted_arr1[i])
            i+=1

        else:
            sorted_list.append (sorted_arr2[ j ])
            j += 1

    # if first condition is true append the element directly
    while i < len_arr1:
        sorted_list.append (sorted_arr1[ i ])
        i += 1

    # if second condition is true append the element directly
    while j < len_arr2:
       sorted_list.append (sorted_arr2[ j ])
       j += 1

    return sorted_list


# print(merged_sorted_array(sorted_arr1,sorted_arr2))

arr = [9,4,6,2,4,8,1]
print(mergeSort(arr))








# let len_arr1 be the length of arr1
# ''' len_arr2 '''''''''''''' arr2

# len_arr1 = len (sorted_arr1)
# len_arr2 = len (sorted_arr2)
#
#
# def mergeSort (arr):
    # specif the exit condition first
    # ''' if we have only one element or
    #  no element simply return that array'''
    # if (len (arr) <= 1):
    #     return arr

    # find the middle element from unsorted array
    # middle = len (arr) // 2

    # 2 pointers left, right
    # left = [:middle]  # starting left (from 0 to middle element)
    # right = [middle:]  # starting right (from middle to end of list)

    # we need to call merSort function on both left and right arr
    # left = mergeSort (left)  # return sorted left arra
    # right = mergeSort (right)  # return sorted right arra

    #  once we got sorted left and right we will mearge them
    # return merged_sorted_list (left, right)

    # function to merge 2 sorted arra
    # def merged_sorted_list (sorted_arr1, sorted_arr2):
    #     merged_sorted_arr = [ ]
    #     # starting both from 0
    #     i = j = 0
    #     while (i < len_arr1) and (j < len_arr2):
    #         if sorted_arr1[ i ] < sorted_arr2[ j ]:
    #             merged_sorted_arr.append (sorted_arr1[ i ])
    #             i += 1
    #         else:
    #             merged_sorted_arr.append (sorted_arr2[ j ])
    #             j += 1
    #     while i < m:
    #         merged_sorted_arr.append (sorted_arr1[ i ])
    #         i += 1
    #
    #     while j < n:
    #         merged_sorted_arr.append (sorted_arr2[ j ])
    #         j += 1
    #     return merged_sorted_arr

    # print (merged_sorted_list (sorted_arr1, sorted_arr2))

    # Now lets consider an unsorted arra
    # arr = [9,4,6,2,4,8,1]
