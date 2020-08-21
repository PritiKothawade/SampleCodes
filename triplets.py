# Input:
# 2
# 4
# 1 5 3 2
# 3
# 3 2 7
# Output:
# 2
# -1
def triplets():
    no_of_test_cases = int(input())
    for test_case in range(no_of_test_cases):
        array_list_len = int(input())
        array_list = list(map(int, input().split()))
        array_list.sort()
        max_ele = array_list[-1]
        array_set = set(array_list)
        count = 0
        for i in range(array_list_len-1):
            for j in range(i+1, array_list_len-1):
                if array_list[i]+array_list[j] > max_ele:
                    break
                if array_list[i]+array_list[j] in array_set:
                    count += 1
        if count >= 1:
            print(count)
        else:
            print(-1)


if __name__ == '__main__':
    triplets()