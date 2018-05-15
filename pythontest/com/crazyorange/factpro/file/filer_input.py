# 根据给定的范围过滤敏感词
##如果输入的输入设定的敏感词 输出freedom
##否则输出human rights
import os
import string


####拿到用户的输入
def getUserPrint():
    input_string = input("please input a words");
    return input_string


####查看过滤词
def filter_conditions(file_path):
    filter_conditions = []
    with open(file_path) as file:
        for line in file:
            filter_conditions.append(line.strip())
    return filter_conditions


####判断输入是否在词组中
def filter(input, conditions):
    if input in conditions:
        print('Freedom')
    else:
        print('Human Rights')


if __name__ == '__main__':
    path='/Users/apple/Desktop/Exercise/Exercise/pythontest/com/crazyorange/filterdir'
    print_words=getUserPrint()
    filter(print_words,filter_conditions(path))

