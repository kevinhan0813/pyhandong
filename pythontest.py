import random
import re
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

'''
str1 = ' GigabitEthernet8.100            10.125.250.25   YES manual up                    up '
result1 = re.match(
    '\s*(\w.*\d)\s+'
    '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+'
    '(\w*)\s+'
    '(\w*)\s+'
    '(\w*)\s+'
    '(\w*)\s*',
    str1
).groups()

print('接口     :'+ result1[0])
print('IP地址   :'+ result1[1])
print('状态     :'+ result1[-1])
'''
'''
import re
str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
result = re.match(
    '\s*(\d{1,3})\s+'
    '(\w{1,4}\.\w{1,4}\.\w{1,4})\s+'
    '(\w*)\s+'
    '(\w.*\d)\s*',
    str1
).groups()

print('VLAN      :'+result[0])
print('MAC       :'+result[1])
print('TYPE      :'+result[2])
print('Interface :'+result[3])
'''

import re

str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710 idle 0:01:09 bytes 27575949 flags UIO'
result = re.match(
    '\s*(\w*)\s+'
    '(\w*)\s+'
    '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5})\s+'
    '(\w*)\s+'
    '(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5})\s+'
    '(\w*)\s+'
    '(\d{1,2}:\d{1,2}:\d{1,2})\s+'
    '(\w*)\s+'
    '(\d{1,10})\s+'
    '(\w*)\s+'
    '(\w*)\s*',
    str1
).groups()

data = result[6].split(':',2) #split是分隔函数，以':'为分隔符,分割成3个

print('{0:15}:{1:15}'.format('prorocol',result[0]))
print('{0:15}:{1:15}'.format(result[1],result[2]))
print('{0:15}:{1:15}'.format(result[3],result[4]))
print('{0:15}:{1}{2}{3}{4}{5}{6}'.format(result[5],data[0],'小时',data[1],'分钟',data[2],'秒'))
print('{0:15}:{1:15}'.format(result[7],result[8]))
print('{0:15}:{1:15}'.format(result[9],result[10]))
