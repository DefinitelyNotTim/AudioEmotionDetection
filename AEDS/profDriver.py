## profDriver.py: A simple driver to test the profile manager
##  Not part of the official software, used for debugging only
from profileManager import *


newP = profileManager("bob")
newPP = profileManager("a")
print(newP.fileName)
newP.accessProfile()
print("\n\n")
newPP.accessProfile()

newPP.writeToProfile([1,2,3,4,5], "angry")
print(newPP.oldMetrics)
