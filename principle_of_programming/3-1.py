class object1():
    __private_value = 3
    _public_value2 = 2
    public_value = 3

    def __init__(self):
        pass

    def __func(self):
        print("I'm private")

    def _func(self):
        print("I'm used as if private, but actually public")

    def func(self):
        print("I'm public")


obj = object1()
