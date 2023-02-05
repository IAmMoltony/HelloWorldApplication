import PrintableString
import StringPrinter
import sys
import subprocess
import importlib.util

def IsPackageInstalled(PackageToCheck):
    Spec = importlib.util.find_spec(PackageToCheck)
    return Spec is not None

def InstallPackage(PackageToInstall):
    InstallPackageString = PrintableString.PrintableString(f"Installing package {PackageToInstall}")
    InstallPackageStringPrinter = StringPrinter.StringPrinter(InstallPackageString)
    InstallPackageStringPrinter.PrintString()
    if IsPackageInstalled(PackageToInstall):
        AlreadyInstalledString = PrintableString.PrintableString("Package is already installed")
        AlreadyInstalledStringPrinter = StringPrinter.StringPrinter(AlreadyInstalledString)
        AlreadyInstalledStringPrinter.PrintString()
        return
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", PackageToInstall])
    except subprocess.CalledProcessError:
        ErrorString = PrintableString.PrintableString(f"There was an error installing package {PackageToInstall}.")
        ErrorStringPrinter = StringPrinter.StringPrinter(ErrorString)
        ErrorStringPrinter.PrintString()
        exit(1)
    InstallPackageStringDone = PrintableString.PrintableString("Done installing package")
    InstallPackageStringDonePrinter = StringPrinter.StringPrinter(InstallPackageStringDone)
    InstallPackageStringDonePrinter.PrintString()

def UpgradePIP():
    UpgradePIPString = PrintableString.PrintableString("Upgrading pip")
    UpgradePIPStringPrinter = StringPrinter.StringPrinter(UpgradePIPString)
    UpgradePIPStringPrinter.PrintString()
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    except:
        ErrorString = PrintableString.PrintableString("There was an error upgrading pip.")
        ErrorStringPrinter = StringPrinter.StringPrinter(ErrorString)
        ErrorStringPrinter.PrintString()
        exit(1)
    UpgradePIPStringDone = PrintableString.PrintableString("Done upgrading pip")
    UpgradePIPStringPrinterDone = StringPrinter.StringPrinter(UpgradePIPStringDone)
    UpgradePIPStringPrinterDone.PrintString()