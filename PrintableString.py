class PrintableString:
    def __init__(TheCurrentInstanceOfThePrintableStringClass, StringContents):
        if type(StringContents) != str:
            raise TypeError("The StringContents parameter passed to the PrintableString class constructor is not of type str.")

        TheCurrentInstanceOfThePrintableStringClass.StringContents = StringContents
    
    def GetContents(TheCurrentInstanceOfThePrintableStringClass):
        return TheCurrentInstanceOfThePrintableStringClass.StringContents