"""
python3中字符串和字节是明确区分的
如果想要修改字符中的某一个片段的字节 只能通过byteArray的形式
"""
data1=b"guojinlong"
print(data1)
#一次性分配内存
data2=bytes("guojinlong","utf-8")
print(data2)
#自动扩展
data3=bytearray("guojinlong",encoding='utf-8')
for strByte in data3:
    print("strbyte:"+str(strByte))

####内存视图，将bytearray转换成内存视图，修改视图中的某个片段
#data3---b'guojinlong'
view=memoryview(data3)
view[0]=105
result=view.tobytes()
#output---b'iuojinlong'
print(result)

