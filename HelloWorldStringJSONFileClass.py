import simplejson

class HelloWorldStringJSONFileClass:
    def __init__(TheCurrentInstanceOfTheHelloWorldStringJSONFileClass):
        with open("HelloWorldString.json") as HelloWorldStringJSONFile:
            TheCurrentInstanceOfTheHelloWorldStringJSONFileClass.HelloWorldStringJSONFileData = simplejson.load(HelloWorldStringJSONFile)

    def GetHelloWorldString(TheCurrentInstanceOfTheHelloWorldStringJSONFileClass):
        return TheCurrentInstanceOfTheHelloWorldStringJSONFileClass.HelloWorldStringJSONFileData["HelloWorldString"]