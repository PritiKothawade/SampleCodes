# Input: arr1[] = {10};
#        arr2[] = {2, 3};
# Output: arr1[] = {2}
#         arr2[] = {3, 10}
#
# Input: arr1[] = {1, 5, 9, 10, 15, 20};
#        arr2[] = {2, 3, 8, 13};
# Output: arr1[] = {1, 2, 3, 5, 8, 9}
#         arr2[] = {10, 13, 15, 20}

def merge(arr1, arr2, n, m):
    l = n if n < m else m
    print(l)
    idx2 = 0
    idx1 = len(arr1)-1
    while idx1 >= 0 and idx2 < len(arr2):
        print(idx1, idx2)
        if arr1[idx1] > arr2[idx2]:
            arr1[idx1], arr2[idx2] = arr2[idx2], arr1[idx1]
            idx2 += 1
        idx1 -= 1
    arr1.sort()
    arr2.sort()
    print(*arr1, end=' ')
    print(*arr2)


if __name__ == '__main__':
    no_of_test_cases = int(input())
    for test_case in range(no_of_test_cases):
        n, m = list(map(int, input().split()))
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        merge(arr1, arr2, n, m)