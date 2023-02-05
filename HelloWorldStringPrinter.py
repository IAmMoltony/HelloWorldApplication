import HelloWorldStringClass
import PrintableString
import StringPrinter

def PrintHelloWorldString(HelloWorldStringObject):
    HelloWorldString = PrintableString.PrintableString(HelloWorldStringObject.GetHelloWorldString())
    HelloWorldStringPrinter = StringPrinter.StringPrinter(HelloWorldString)
    HelloWorldStringPrinter.PrintString()