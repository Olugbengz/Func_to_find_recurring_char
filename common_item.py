# Finding common items in two arrays

arr1 = ['a', 'b', 'c', 'k']
arr2 = ['a', 'j', 'l']

# Naive or brute force approach - O(n^2)

def find_common_item1(arr_1, arr_2):
    for i in range(len(arr_1)):
        for j in range(len(arr_2)):
            if arr_1[i] == arr_2[j]:
                print("True")
    return False


# A better approach with better time complexity - O(n)
def find_common_item2(arr_1, arr_2):
    map = {arr1[i]: "True" for i in range(len(arr_1))}
    for j in range(len(arr_2)):
        if map[arr_2[j]]:
            return True
    return False


result = find_common_item1(arr1, arr2)
result1 = find_common_item2(arr1, arr2)
print(result)