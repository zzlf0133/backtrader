a = 1
print(a.__class__)
print(type(a))
#type是取类的函数
class A:
    pass
print(A.__class__)
print(type(A))
#class本身的类型是type
def f(cls):
    return cls
x = f(A)
#类本身可以作为参数使用
B = type("A",(),{})#创建一个名为"A"的类型B ####B是type的实例（B的type是type）
print(B)
#若a的type是A，则称a为A的实例
###元类：创建类的类
###__new__：控制类的创建
class Meta(type):
    def __new__(cls,name,bases,dct):# type(name,bases,dct)表示创建一个名为name，继承自bases，有dct属性和对应默认值的类，此处用法与之类似
        print(f"creating{name}")
        return super().__new__(cls,name,bases,dct)# Meta继承了type，调用了type.__new__()，cls是self的类，即type(self)
    #本质上是定义了Meta.__new__()，super().__new__(cls)是Meta的父类的类（type）的__new__()方法，即type.__new__()
class A(metaclass = Meta):#metaclass参数决定谁来创建这个类，不同于父类（只继承方法和属性），还会控制创建过程
    pass

class Base:
    def __init_subclass__(cls):#创建子类时自动执行
        print(cls.__name__)

class A(Base):#创建A时，调用Base.init(cls=A)
    pass

#描述符协议
class D:
    def __get__(self, instance, owner):#instance:实例，owner:实例所属的类
        print('get')
        return 42
    def __set__(self, instance, value):
        print('set')
        instance._x = value  # __set__的返回值会被忽略，应存储值而非return
class A:
    x = D()#A.x是一个类
a=A()
print(a.x)#执行get，self=x,instance = a, owner = A
a.x=10#执行set