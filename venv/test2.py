class Test:

    def __init__(self, name):
        print("Test created")
        self.name = name

    def hello(self):
        print("hello")

    def get_name(self):
        return self.name


d = Test("d")

print(type(d))
