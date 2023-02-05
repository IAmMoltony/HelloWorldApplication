import subprocess
import sys
import StringPrinter
import PrintableString
import PackageInstaller
import DependencyListParser

def DependencyInstallerMain():
    DependencyInstallerWelcomeString = PrintableString.PrintableString("Welcome to the Dependency Installing module of the Hello World Application.")
    DependencyInstallerWelcomeStringPrinter = StringPrinter.StringPrinter(DependencyInstallerWelcomeString)
    DependencyInstallerWelcomeStringPrinter.PrintString()

    PackageInstaller.UpgradePIP()

    DependenciesToInstall = DependencyListParser.ParseDependencyList("DependencyList.txt")
    for Dependency in DependenciesToInstall:
        PackageInstaller.InstallPackage(Dependency)

    DependencyInstallerFinishedString = PrintableString.PrintableString("Dependency Installer has finished installing the required dependenciies for the Hello World Application.\nNow you can use the following line to run the Hello World Application:\npython (or python3, depending on your OS) HelloWorldApplication.py")
    DependencyInstallerFinishedStringPrinter = StringPrinter.StringPrinter(DependencyInstallerFinishedString)
    DependencyInstallerFinishedStringPrinter.PrintString()

if __name__ == "__main__":
    DependencyInstallerMain()
else:
    ErrorString = PrintableString.PrintableString("The DependencyInstaller.py script should not be imported.")
    ErrorStringPrinter = StringPrinter.StringPrinter(ErrorString)
    ErrorStringPrinter.PrintString()
    exit(1)