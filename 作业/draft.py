class AutoParams(type):
    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        print(type(obj))  # 看看是什么
        return obj


class A(metaclass=AutoParams):
    pass


a = A()