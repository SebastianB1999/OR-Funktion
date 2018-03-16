__version__ ="1.5"
__author__ = "Sebastian Bensing"

class AndGate(object):
    """description of class"""


    def __init__(self, *args, **kwargs):
        self.__Input0 = False
        self.__Input1 = False
        self.__Output = False
        self.__Name = "AndGate"
        return super().__init__(*args, **kwargs)

    def execute(self):
        if Input0 == True:
            if Input1 == True:
                Output = True

    def show(self):
        print("Die Bedingungen sind: "+__str__(self.__Output))

    def __str__(self,wert):
        return str(wert)
        return super().__str__()

    # getter/setter
   
    def __setInput0(self,value):
        isinstance(value, bool)
        self.__Input0 = wert

    def __setInput1(self,wert):
        isinstance(value, bool)
        self.__Input1 = wert

    def __getInput0(self):
        return self.__Input0

    def __setName(self, value):
        isinstance(value, str)
        self.__Name = value

    def __getInput1(self):
        return self.__Input1

    def __getName(self):
        return self.__Name

    def __getOutput(self):
        return self.__Output

    def __setOutput(self,value):
        isinstance(value, bool)
        self.__Output = wert

    # property

    Name = property(__getName,__setName)
    Input0 = property(__getInput0,__setInput0)
    Input1 = property(__getInput1,__setInput1)
    Output = property(__getOutput,)