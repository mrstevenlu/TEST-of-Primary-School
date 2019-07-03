# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Steven Lu

# 目的:
# 写第一套程序
# 小学试卷
import random


print("----小学四则计算题----")
filename1 = "TEST of Primary School.txt"
filename2 = "TEST of Primary School(含答案).txt"


f1 = open(filename1, 'w')
line1 = "----小学四则运算题----\n"
f1.write(line1)

f1.close()


f2 = open(filename2, 'w')
line2  = "----小学四则运算题（含答案）----\n"
f2.write(line2)

f2.close()


f1 = open(filename1,'a')
f2 = open(filename2,'a')

count=0


for row in range(1,21):
    line1= ''
    line2= ''
    for col in range(1,6):
        count =count + 1

        a = random.randint(1, 100)
        b = random.randint(1, 100)

        op = random.randint(1, 4)


        if op == 1:
            line1 = line1 + "%0.2f + %0.2f = \t\t\t" % (a, b)
            answer=a + b
            line2 = line2 + "%0.2f + %0.2f =%0.2f \t\t\t" % (a, b,answer)

        if op == 2:
           if a>=b:
               line1 = line1 + "%0.2f - %0.2f = \t\t\t" % (a, b)
               answer=a - b
               line2 = line2 + "%0.2f - %0.2f =%0.2f \t\t\t" % (a, b,answer)
           else:
               line1 = line1 + "%0.2f - %0.2f = \t\t\t" % (b, a)
               answer=b - a
               line2 = line2 + "%0.2f - %0.2f =%0.2f \t\t\t" % (b, a,answer)

        if op == 3:
            line1 = line1 + "%0.2f × %0.2f = \t\t\t" % (a, b)
            answer=a * b
            line2 = line2 + "%0.2f × %0.2f =%0.2f \t\t\t" % (a, b,answer)

        if op == 4:
           if a>=b:
               line1 = line1 + "%0.2f ÷ %0.2f = \t\t\t" % (a, b)
               answer=a / b
               line2 = line2 + "%0.2f ÷ %0.2f =%0.2f \t\t\t" % (a, b,answer)
           else:
               line1 = line1 + "%0.2f ÷ %0.2f = \t\t\t" % (b, a)
               answer=b / a
               line2 = line2 + "%0.2f ÷ %0.2f =%0.2f \t\t\t" % (b, a,answer)


    line1 += "\n"
    f1.write(line1)

    line2 += "\n"
    f2.write(line2)


print("----结束----总共出了{0}道四则运算题".format(count))

line1="----结束----总共出了{0}道四则运算题".format(count)
line2="----结束----总共出了{0}道四则运算题".format(count)

f1.write(line1)
f2.write(line2)

f1.close()
f2.close()
