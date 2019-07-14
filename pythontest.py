import random

'''
str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))

print(str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))+'.'+str(random.randint(1,255))) #随机生成IP地址

test = 'QYTANG'+'\''+'day'+' '+'2014-9-28' #字符串拼接
print(test)

str1 = 'QYTANG' #字符串拼接
str2 = '\''
str3 = 'day'
str4 = ' 2014-9-29'
print(str1+str2+str3+str4)

word = 'csallywag' #通过切片创建子字符串
sub_word = word[2:-3]
print(str(sub_word))


str1 = 'Python' #切片游戏
str2 = str1[1:]
str3 = '-'
str4 = str1[0]
str5 = 'y'
print(str2+str3+str4+str5)
'''

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FREE_SEC = 456789.12456
COURSE_FREE_PYTHON = 1234.3456

'''
line1 = String formatting expressions:'...%s...'%(values)
line2 =
'''
import re

str1 = ' GigabitEthernet8.100           10.125.250.25   YES manual up                    up '
result1 = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*)\s*',str1).groups()

print('接口     :'+ result1[0])
print('IP地址   :'+ result1[1])
print('状态     :'+ result1[-1])
