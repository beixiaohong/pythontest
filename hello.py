# 输出功能联系
'''
str='123456789'
print("输出字符串:",str)                 # 输出字符串
print("输出第一个到倒数第二个的所有字符"+str[0:-1])           # 输出第一个到倒数第二个的所有字符
print("输出字符串第一个字符"+str[0])              # 输出字符串第一个字符
print("输出从第三个开始到第五个的字符"+str[2:5])            # 输出从第三个开始到第五个的字符
print("输出从第三个开始后的所有字符"+str[2:])             # 输出从第三个开始后的所有字符
print("输出从第二个开始到第五个且每隔一个的字符（步长为2）"+str[1:7:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print("输出字符串两次"+str * 2)             # 输出字符串两次
print("连接字符串"+str + '你好')         # 连接字符串
print("输出字符串两次2 "+str * 2, end = "");             
print(r"  \n连接字符串2 "+str + '你好')         # 连接字符串
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
'''

 
print('------------------------------')

# print('请输入第一个数字')
# num1 = input()
# 打印提示信息，表示开始四则运算练习
print('现在我开始练习四则运算')

# 获取用户输入的第一个数字，转换为整数类型
num1 = input('请输入第一个数字')
num1 = int(num1)

# 获取用户输入的第二个数字，同样转换为整数类型
num2 = input('请输入第二个数字')
num2 = int(num2)

# 计算并打印数字之和
print('你输入的数字和是：', num1 + num2)

# 计算并打印数字之差
print('你输入的数字差是：', num1 - num2)

# 计算并打印数字之积
print('你输入的数字积是：', num1 * num2)

# 计算并打印数字之商（浮点数结果）
print('你输入的数字商是：', num1 / num2)

# 计算并打印第一个数字的第二个数字次幂
print('你输入的数字幂是：', num1 ** num2)