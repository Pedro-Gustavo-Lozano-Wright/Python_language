
def singleton1():

    class Singleton(type):

        def __init__(cls, name, bases, attrs, **kwargs):
            super().__init__(name, bases, attrs)
            cls._instance = None

        def __call__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__call__(*args, **kwargs)
            return cls._instance

    class MyClass(metaclass=Singleton):
        def __init__(self, name=""):
            self.name = name  # variabl publica

        def preguntar_nombre(self):
            print("Hola soy " + self.name)

    m1 = MyClass("gus")
    m2 = MyClass()
    m2.preguntar_nombre()
    if id(m1) == id(m2):
        print("Singleton")
    else:
        print("Otro objeto")












def singleton2():

    class SingletonMeta(type):

        _instances = {}

        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]

    class Singleton(metaclass=SingletonMeta):

        def __init__(self, name=""):
            self.name = name  # variabl publica

        def preguntar_nombre(self):
            print("Hola soy " + self.name)

        def some_business_logic(self):
            pass

    s1 = Singleton("gus")
    s1.preguntar_nombre()
    s2 = Singleton()
    s2.name = "loz"
    s1.preguntar_nombre()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")

