class Model:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def add(a,b,c):
        return a+b+c
obj=Model()
obj.add(1,2)    #Error :  TypeError: Model.add() missing 1 required positional argument: 'c'
obj.add(1,2,3)