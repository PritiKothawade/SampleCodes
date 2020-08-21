# Input
# 2
# 5
# 1 2 3 -2 5
# 4
# -1 -2 -3 -4
# Output
# 9
# -1
def maxSubArraySum(l):

    positiveCheckList = [1 for i in l if i > 0]
    if any(positiveCheckList):
        global_max = 0
        current_max = l[0]
        for i in l:
            current_max = max(i, current_max+i)
            if current_max > global_max:
                global_max = current_max
        return global_max
    else:
        return max(l)


if __name__ == "__main__":
    print(maxSubArraySum([1,-2,3,4,-5,8]))