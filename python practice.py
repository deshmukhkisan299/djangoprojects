# def abc():
#     a=10
#     print("hi")
#     return a
# abc()
#
# def abc(b):
#     if (b<6):
#         a=10
#         c = b+abc(b-1)
#         print(c)
#     return c
#
# abc(3)
# def recursion(k):
#     n = 0
#     if(k>0):#2>0
#         n = 1+ recursion(k-1)#recursion(1)=if 1>0:n = 1+0,#0>hence return n=0
#         print(recursion(k-1))
#         # k = n
#         # print(k)
#     return n
# print("recursion::3")
# recursion(3)
# print("recursion::2")
# recursion(2)
# print("recursion::1")
# recursion(1)
#
#
# """
# 4=10,
# 10+10
#
#
# """
# 0
# 0
# 1
# 0
# 0
# 1
# 0
# 0
# 1
# 2
# 0
# 0
# 1
# 2
# 3
# 0
# 0
# 1
# 2
# 3
# 4
#
#
#
#
import requests
import json
import pandas as pd
url = requests.get('https://www.worldometers.info/coronavirus/')#.json()

df = pd.DataFrame(url)
print(df)


