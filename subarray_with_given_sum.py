# Input:
# 2
# 5 12
# 1 2 3 7 5
# 10 15
# 1 2 3 4 5 6 7 8 9 10
# Output:
# 2 4
# 1 5

def find_range():
    no_of_test_cases = int(input())
    for test_case in range(0, no_of_test_cases):
        size_of_array, total = list(map(int, input().split()))
        array_list = list(map(int, input().split()))
        cur_sum = 0
        start_idx = 0
        end_idx = 0
        while end_idx < len(array_list)+1:
            if cur_sum == total:
                print(start_idx+1, end_idx)
                break
            elif cur_sum > total and end_idx != len(array_list)+1:
                cur_sum -= array_list[start_idx]
                start_idx += 1
            elif cur_sum < total and end_idx != len(array_list):
                cur_sum += array_list[end_idx]
                end_idx += 1
            else:
                print(-1)
                break


if __name__ == '__main__':
    find_range()