# Input:
# 2
# 6
# 1 2 3 4 5 6
6
# 11
# 10 20 30 40 50 60 70 80 90 100 110
#
# Output:
# 6 1 5 2 4 3
# 110 10 100 20 90 30 80 40 70 50 60


def rearrange(arr, l):
    i = l-1
    k = 0
    while k < i:
        temp = arr[-1]
        j = l - 1
        while j > k:
            arr[j] = arr[j-1]
            j = j - 1
        arr[k] = temp
        k = k + 2
    return arr


if __name__ == '__main__':
    no_of_test_cases = int(input())
    for test_case in range(no_of_test_cases):
        length = int(input())
        arr = list(map(int, input().split()))
        print(rearrange(arr, length))
