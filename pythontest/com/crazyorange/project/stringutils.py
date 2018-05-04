"""
1.使用正则表达式拆分具有多种分隔符的字段
"""
import re
s='abd/hh,heihei\tguo|'
result=re.split('[/,\t|]',s)
print(result)


"""
2.判断一个字符串是否以 某个字母开头或者结尾
使用字符串的startWith或者endWith
例如url的开头，文件的结尾
"""
fileName='string.py'
filter_result=fileName.endswith(('.pdf','.py','.txt'))
print(filter_result)

"""
字符串中的文本格式
正则表达式的捕获组 re.sub(),
第一个参数：要捕获的字符串的规则，每一个的正则表达式用（）括起来，并且给组进行命名?P<group name>。
第二个参数：将获取到的每组数据根据组的名字进行重新排序
这里首先会匹配字符串中符合整个正则表达式的字符串（年-月-日），并且将年，月，日分成三组，
根据新的规则重新排序，生成新的字符串
05/12/2016sss，09/01/2016ddd，05/19/2018aaa
"""
str="2016-05-12sss，2016-09-01ddd，2018-05-19aaa"
r1=re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})',r'\g<month>/\g<day>/\g<year>',str)
print(r1)


"""
使用str的join方法进行字符串拼接
"""
s1="sss"
s2="1111"
s3="ccc"
join="".join([s1,s2,s3])
print(join)



"""
左右对齐输出字符串
在左边，右边填充字符，不指定字符就是空格
s.rjust(20,'='),s.ljust(20),s.center(10)
"""



"""
去掉字符串中不需要的字符
1.replace 替换一种字符
2.同时替换多种字符 re.sub可以使用正则表达式进行替换
"""
translate="assdsdsxyz"
result=translate.translate(['xyz','111'])
print(result)
