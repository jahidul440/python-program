"Given an unsorted array and another sorted array sort the first and find common elements (No duplicates)"
# Basic solution: Selection sort
# Find smallest element in unsorted_array and then compare it to current smallest element in sorted_array, add it if equal
# if sorted_array element is smaller advance sorted_array iterator
# Complexity: O(n^2)
import time 
def Simple(unsorted_array, sorted_array):
    time_sec = int(round(time.time() * 1000))
    arr = unsorted_array[:]
    sorted_index = 0
    commonElements = []
    # Iterate over the array
    for i in range(len(arr)):  
        # value of the smallest element 
        smallestIndex = i
        # Iterate over the array to find smallest element
        for j in range(i+1, len(arr)): 
            if arr[j] < arr[smallestIndex]: 
                smallestIndex = j
        # compare smallest element in arr to smallest in arr2
        while (sorted_array[sorted_index] < arr[smallestIndex] and sorted_index < len(sorted_array)-1):
            sorted_index += 1
        if (sorted_array[sorted_index] == arr[smallestIndex]):
            if (arr[smallestIndex] not in commonElements):
                commonElements.append(arr[smallestIndex])
            sorted_index += 1
        arr[i], arr[smallestIndex] = arr[smallestIndex], arr[i]
    print("0.",time_sec)    
    print("Basic:    {0}".format(commonElements))

        

# Test 1
arr1 =  [1, 2, 3, 4, 5, 5]
arr2 =  [0, 1, 3, 5, 5, 6]
Simple(arr1, arr2)

# Test 2
arr1 =  [5, 3, 10, 3, 0, 0, 1, 9, 3, 9]
arr2 =  [1, 4, 5, 7, 7, 8, 8, 9, 9, 10]
Simple(arr1, arr2)
# Test 3
arr1 =  [2, 2, 2, 1, 1, 1, 0, 0, 0]
arr2 =  [0, 1, 3, 5, 5, 6]
Simple(arr1, arr2)
# Test 4
arr1 =  []
arr2 =  []
Simple(arr1, arr2)
# Test 5
arr1 =  ['z', 'q', 'w', 'o', 'i', 'b', 'b', 'a']
arr2 =  ['a', 'b', 'b', 'h', 'o', 'p', 's', 'z']
Simple(arr1, arr2) 


