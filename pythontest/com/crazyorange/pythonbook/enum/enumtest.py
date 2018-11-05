"""
枚举
1.引入枚举包
2.继承枚举类
"""
#1
import enum
Color1=enum.Enum("AA","Black Yellow Red")

#2
class Color(enum.Enum):
    Yellow="Yellow"
    Red="Red"


print(Color.Red.name)