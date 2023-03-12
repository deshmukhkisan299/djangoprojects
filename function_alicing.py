# def abc():
#     print("abc")
#     def bcd():
#         print("in bcd")
#         def cde():
#             print("in cde")
#         return cde
#     return bcd
#
# a = abc()
# b = a()
# c = b()
# print(type(b))
#
# # c =b
# # d= c
# # e = d
# # f = e
# # # print(type(abc))
# # # print(type(abc()))
# # b
# # print(type(a))
# # print(type(f))
# import function_alicing
# function_alicing.abc()
def abc():
    print("in abc")
    def bcd():
        print("in bcd")
    return bcd

a = abc
b= a()
b()
print(type(b()))

