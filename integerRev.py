def intRev(no):
    revInteger = []
    while(no):
       revInteger.append(str(no%10))
       no = no//10
    return ''.join(revInteger)


# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = -1 if x<0 else 1
#         x = str(abs(x))
#         x = int(x[::-1])
#         if x > (pow(2,31)-1) or x < pow(-2,31):
#             return 0
#         return x*sign
#
# class Solution:
#     def reverse(self, x: int) -> int:
#         sign = -1 if x < 0 else 1
#         y = abs(x)
#         r = 0
#         while y:
#             r = r * 10 + y % 10
#             y = y // 10
#         if r > (pow(2, 31) - 1) or r < pow(-2, 31):
#             return 0
#         return r * sign


if __name__ == '__main__':
    print(intRev(1234))