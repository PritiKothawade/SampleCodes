# # code
#
# Input:
# 2
# 5
# 1 2 3 5
# 10
# 1 2 3 4 5 6 7 8 10
#
# Output:
# 4
# 9

def missing(arr, l):
    expected_sum = sum([n for n in range(1, l+1)])
    actual_sum = sum(arr)
    return expected_sum-actual_sum


if __name__ == '__main__':
    no_of_test_cases = int(input())
    for test_case in range(no_of_test_cases):
        length = int(input())
        arr = list(map(int, input().split()))
        print(missing(arr, length))

