class AutoParams(type):
    def __call__(cls, *args, **kwds):
        obj = super().__call__(*args, **kwds)
        obj.p = {}

        for base in reversed(cls.__mro__):
            if hasattr(base,'params'):
                obj.p.update(base.params)
        return obj
class A(metaclass = AutoParams):
    params = {'period':14}
a=A()
print(a.p)