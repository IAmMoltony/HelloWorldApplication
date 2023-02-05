import HelloWorldStringGetter

class HelloWorldStringClass:
    def __init__(TheCurrentInstanceOfTheHelloWorldStringClass):
        TheCurrentInstanceOfTheHelloWorldStringClass.HelloWorldString = HelloWorldStringGetter.GetHelloWorldString()
    
    def GetHelloWorldString(TheCurrentInstanceOfTheHelloWorldStringClass):
        return TheCurrentInstanceOfTheHelloWorldStringClass.HelloWorldString