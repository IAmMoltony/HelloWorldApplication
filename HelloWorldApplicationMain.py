import HelloWorldStringClass
import HelloWorldStringPrinter

def HelloWorldMain():
    HelloWorldStringObject = HelloWorldStringClass.HelloWorldStringClass()
    HelloWorldStringPrinter.PrintHelloWorldString(HelloWorldStringObject)

if __name__ == "__main__":
    HelloWorldMain()
else:
    print("The HelloWorldApplicationMain.py script should not be imported.")
    exit(1)