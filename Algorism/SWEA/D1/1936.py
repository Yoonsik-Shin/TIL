class MyClass:

    def method(self):
        return 'instance method', self

    @classmethod
    def classmethod(cls):
        return 'class method', cls

test1 = MyClass()
print(test1.method())
print(test1.classmethod())
