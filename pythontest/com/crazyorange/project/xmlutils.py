"""
xml csv json 解析方式
"""
"""
csv数据解析的方式
可以使用标准库中的csv模块
"""
import csv

# with open('pingan.csv', 'rb') as file:
#     csv_data = csv.reader(file)
# ###读取数据
# for data in csv_data:
#     print(data)
# ####写入数据
# write_file = open('pingan.csv', 'wb')
# csv_write = csv.writer(write_file)
# csv_write.writerow(['data', 'haha'])

"""
解析json数据
"""
import json
a="{'a':'b'}"
###可以将一个python对象转换成json
json_result=json.dumps(a)
print(json_result)

###将json字符串转换成python对象
l2=json.loads('{"a":13}')
print(l2)