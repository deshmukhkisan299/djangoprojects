"""
OOP::  Object oriented
bottom -up approach
"""
#
# class Dell:
#     def laptop(self):


class laptop:
    def __init__(self,ram,screensize,processor):
        self.ram = ram #instance
        self.screensize = screensize
        self.processor = processor


    def hp_s1(self, camera):
        a=15 #local
        self.camera = camera
        print("Camera:: ",self.camera)
        print("ram:: ",self.ram)
        print("Screen:: ",self.screensize)
        print("Processor:: ",self.processor)

    def hp_s2(self, camera, network):
        a=15 #local
        self.network = network
        self.camera = camera
        print("Camera:: ",self.camera)
        print("Network:: ",self.network)
        print("ram:: ",self.ram)
        print("Screen:: ",self.screensize)
        print("Processor:: ",self.processor)


    def hp_s3(self, network):
        a=15 #local
        self.network = network
        print("Network:: ",self.network)
        print("ram:: ",self.ram)
        print("Screen:: ",self.screensize)
        print("Processor:: ",self.processor)

# obj = laptop(4,19,24)
# obj.hp_s3("5g")

# laptop: class
#
# dell, hp: object
#
# ram, rom, screensize: property
# class
# object
# method
# a =5
"""
class = its an global identity
method = functions in class or features
properties = 
object = its an real time entity


"""
class test:#static variable or class variable
    def __init__(self,initname):
        self.name = initname #instance variable or class variable
         #instance variable or class variable
    def function1(self,name1,classs):
        a = 100
        self.name1= name1
        self.classs = classs
        print("obj1")
        print("Name::",self.name1)
        print("class::",self.classs)
        print()
    def function2(self,city):
        print("obj2")
        print("Name::",self.name)
        print("class::",self.classs)
        print("class::",city)
        print()

obj= test('Krishna')
obj1 = obj.function1("mohan",5)
obj2 = obj.function2("pune")
# class test2:
#     def function1(self):
#         print(test.name)
# objt1= test('Krishna')
# objt1_1 = obj.function1("mohan",5)
# objt1_2 = obj.function2("pune")
# objt2 = test2()
# objt2_1 = obj2.function1()

