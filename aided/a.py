from random import randint
import cellLibrary
import os
childname = cellLibrary.appendName(os.path.basename(__file__))
child = open(childname, "w")
parent = open(os.path.basename(__file__), "r")
child.write(cellLibrary.mutate(parent.read()))
os.system("start python "+childname+" 1")
os.system("start python "+os.path.basename(__file__)+" 1")