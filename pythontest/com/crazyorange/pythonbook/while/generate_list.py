##列表生成表达式
list=[x+10 for x in range(15) if x%2==0]
print(list)

map={k+"-":v for k,v in zip('abcde','12345')}
print(map)

#针对不同元素 可以有多个列表解析式
map2={k:v for k in "abcdef" if isinstance(k,str)
      for v in range(5) if isinstance(v,int)}
print(map2)