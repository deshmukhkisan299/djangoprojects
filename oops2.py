# class flat:
#     def __int__(self, area):
#         self.area = area
#
#
#
#     def t1(self, length, width, others, area):
#         self.area = area
#         print('area:', self.area)
#         print('length:', length)
#         print('width:', width)
#         print('others:', others)
#
#     # def t2(self, length, width, balcony, area):
#     #     print('area:', self.area)
#     #     print('length:', length)
#     #     print('width:', width)
#     #     print('balcony:', balcony)
#
#
# obj = flat()
# obj.t1(100, 200, '2BHK','jhg')
class flat:
    def __init__(self, area):
        self.area = area

    def t1(self, length, width, others):
        print('area:', self.area)
        print('length:', length)
        print('width:', width)
        print('others:', others)

    def t2(self, length, width, balcony):
        print('area:', self.area)
        print('length:', length)
        print('width:', width)
        print('balcony:', balcony)


obj = flat('abc')
obj.t1(100, 200, '2BHK')
obj.t2