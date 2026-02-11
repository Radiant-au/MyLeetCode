from typing import List


def prefix(arr : List) -> List:
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1 , len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
        
    return prefix

def suffix(arr : List) -> List:
    n = len(arr)
    suffix = [0] * n
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2 , -1 , -1):
        suffix[i] = suffix[i + 1] + arr[i]
        
    return suffix 

arr = [1,2,3,4]
print(suffix(arr))