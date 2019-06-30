# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Steven Lu

# 目的:
# 写第一套程序
# 小学试卷
import random


print("----小学四则运算题----")
filename = "TEST of Primary School.txt"

f = open(filename, 'w')  # write 方式第一次写一行
text2write = "----开始出题目----\n"
f.write(text2write)

f.close()

f = open(filename,'a')
count=0

#for i in range(1,100):
    #count=count+1

for row in range(1,21):
    line1= ''
    for col in range(1,6):
        count =count + 1


        a = random.randint(0, 99)
        b = random.randint(0, 99)

        op = random.randint(1, 4)
        #当op=4 时是加法
        if op == 1:
            line1 = line1 + "%d + %d = \t" % (a, b)
            #print(line1)

        #当op=4 时是减法
        if op == 2:
            line1 = line1 + "%d - %d = \t" % (a, b)
            #print(line1)

        #当op=4 时是乘法
        if op == 3:
            line1 = line1 + "%d * %d = \t" % (a, b)
            #print(line1)

        #当op=4 时是除法
        if op == 4:
            line1 = line1 + "%d / %d = \t" % (a, b)
            #print(line1)

        # print('现在打印第{0}行-第{1}列-第{2}道数学题'.format(row,col,count))

    print(line1)
    text2write = line1 + '\n'
    f.write(text2write)
    #print("\n")
print("----结束----总共出了{0}道四则运算题".format(count))


text2write="----结束----总共出了{0}道四则运算题".format(count)

f.write(text2write)


f.close()
