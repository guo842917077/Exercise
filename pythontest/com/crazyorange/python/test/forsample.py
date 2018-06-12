###循环练习
"""
在python中 使用if 不需要（），根据缩紧来判断，条件后面要加:号
int()方法相当于java中的parseInt 将字符串转化为int
"""
print("please input a number")
a = input('number is : ')
if int(a) < 3:
    print("excute a<3")
    print("haha")
elif int(a) == 3:
    print("excute a==3")
    print("heihei")
else:
    print("excute else")

numbers = (1, 2, 3, 4, 5, 6, 7, 8)
"""
python的for循环 x 表示声明的变量 在循环时它相当于集合中的每一个变量
"""
for x in numbers:
    if x == a:
        print(x)

n = 0
while n < len(numbers)-1:
    n = n + 1
    print("n : %s" % (n))
    if numbers[n] == a:
        print("find a in numbers : %s" % (n))
        break
