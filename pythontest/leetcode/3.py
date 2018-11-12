"""
leetcode
反转整数
1。通过让原数不断%10的方式，取出个位的余数，记录下来
2。让余数在迭代时不断乘以10来进位，这样越早出来的数，乘10的次数越多，进位越快
3。让原数据/10，通过舍弃余数的方式不断抛除个位数

利用了在迭代过程中取余数 *10 进位的思想
利用了向上进位 思想舍弃每次迭代的个位数
"""


def reverse(x):
    # 记录下反转的数
    reverse = 0
    if x == 0:
        return 0
    if x < 0:
        x = -x
        while x != 0:
            # 每一次轮训获取数据的个位数 在下一次乘以10进行进位
            reverse = reverse * 10 + x % 10
            # 舍弃数据中的个位数
            x = int(x / 10)
        # 因为x本身是负数 ，所以还原
        reverse = -reverse
    else:
        while x != 0:
            reverse = reverse * 10 + x % 10
            x = int(x / 10)
    # 值必须在2 31次幂 减1 到 -2的31次幂之间
    if reverse > (pow(2, 31) - 1) or reverse < (pow(-2, 31)):
        return 0

    return reverse


x = reverse(-123)
print(x)
