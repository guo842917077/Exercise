"""
range：输出从第一个位置开始，在到达第二个位置结束个数字 组成集合
第三个参数表示 隔多少位输出一次
"""
a=list(range(1,5))
print(a)
##[2,4,6,8,10]
b=list(range(2,11,2))
print(b)
"""
列表解析式
1.给定一个公式
2.指定一个for循环负责给value提供值
"""
b=[value**2 for value in range(1,11)]
print(b)

c=[value*1 for value in range(1,100000)]
#计算总和
print(sum(c))
#计算最大值
print(max(c))