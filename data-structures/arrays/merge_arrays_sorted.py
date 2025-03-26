# Create a function that merges two array into a big one sorted
# Input: [0, 3, 4, 31] [4, 6, 30]
# Result: [0, 3, 4, 4, 6, 30, 31]

def mergeSortedArray(array1, array2):
    merged_array = []
    count_array1 = 0
    count_array2 = 0

    while True:
        if count_array1 < len(array1) and count_array2 < len(array2):
            if array1[count_array1] <= array2[count_array2]:
                merged_array.append(array1[count_array1])
                count_array1 += 1
            else:
                merged_array.append(array2[count_array2])
                count_array2 += 1

        elif count_array1 < len(array1):
            merged_array.append(array1[count_array1])
            count_array1 += 1

        elif count_array2 < len(array2):
            merged_array.append(array2[count_array2])
            count_array2 += 1
    
        if len(merged_array) == (len(array1) + len(array2)):
            break
        
    return merged_array

result = mergeSortedArray([0, 3, 4, 31], [4, 6, 30])
print(result)