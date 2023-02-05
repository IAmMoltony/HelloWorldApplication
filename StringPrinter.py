import PrintableString

class StringPrinter:
    def __init__(TheCurrentInstanceOfTheStringPrinterClass, StringToPrint):
        if not isinstance(StringToPrint, PrintableString.PrintableString):
            raise TypeError(f"The StringToPrint parameter passed to the StringPrinter class constructor is not a PrintableString.")
        TheCurrentInstanceOfTheStringPrinterClass.StringToPrint = StringToPrint

    def PrintString(TheCurrentInstalceOfTheStringPrinterClass):
        print(TheCurrentInstalceOfTheStringPrinterClass.StringToPrint.GetContents()) # TODO is there a library that we can use to print things instead of the built in print()?