# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start_idx = 0
        end_idx = len(nums) - 1
        arr = sorted(nums)
        while start_idx < end_idx:
            cur_sum = arr[start_idx] + arr[end_idx]
            if cur_sum == target:
                i = nums.index(arr[start_idx])
                j = nums.index(arr[end_idx], i+1) if arr[start_idx] == arr[end_idx] else nums.index(arr[end_idx])
                return [i,j] if i<j else [j,i]
            elif cur_sum > target:
                end_idx -= 1
            else:
                start_idx += 1
        return -1


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            if target - v in nums[i + 1:]:
                return (i, nums.index(target - v, i + 1))
        return -1
