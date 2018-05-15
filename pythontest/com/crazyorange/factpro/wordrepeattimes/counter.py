"""
统计文本中某个词的出现频率
"""
import re
from collections import Counter
path = '/Users/apple/Desktop/workspace/opensource/Glide/checkstyle.xml'
content = ''
with open(path, mode='r', encoding='utf-8') as file:
    content = file.read()

result=re.split('\W+',content)
counter=Counter(result)
print(counter.most_common(3))

