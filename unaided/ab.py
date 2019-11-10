from random import randint
import os
import math
print(os.path.basename(__file__))
childname = list(os.path.basename(__file__))
random0 = randint(0,len(childname)-4)
random1 = randint(1,36)
newChar = ""
if(random1 == 1):
	newChar = "a"
elif(random1 == 2):
	newChar = "b"
elif(random1 == 3):
	newChar = "c"
elif(random1 == 4):
	newChar = "d"
elif(random1 == 5):
	newChar = "e"
elif(random1 == 6):
	newChar = "f"
elif(random1 == 7):
	newChar = "g"
elif(random1 == 8):
	newChar = "h"
elif(random1 == 9):
	newChar = "i"
elif(random1 == 10):
	newChar = "j"
elif(random1 == 11):
	newChar = "k"
elif(random1 == 12):
	newChar = "l"
elif(random1 == 13):
	newChar = "m"
elif(random1 == 14):
	newChar = "n"
elif(random1 == 15):
	newChar = "o"
elif(random1 == 16):
	newChar = "p"
elif(random1 == 17):
	newChar = "q"
elif(random1 == 18):
	newChar = "r"
elif(random1 == 19):
	newChar = "s"
elif(random1 == 20):
	newChar = "t"
elif(random1 == 21):
	newChar = "u"
elif(random1 == 22):
	newChar = "v"
elif(random1 == 23):
	newChar = "w"
elif(random1 == 24):
	newChar = "x"
elif(random1 == 25):
	newChar = "y"
elif(random1 == 26):
	newChar = "z"
elif(random1 == 27):
	newChar = "0"
elif(random1 == 28):
	newChar = "1"
elif(random1 == 29):
	newChar = "2"
elif(random1 == 30):
	newChar = "3"
elif(random1 == 31):
	newChar = "4"
elif(random1 == 32):
	newChar = "5"
elif(random1 == 33):
	newChar = "6"
elif(random1 == 34):
	newChar = "7"
elif(random1 == 35):
	newChar = "8"
elif(random1 == 36):
	newChar = "9"
while newChar == list(childname)[random0]:
	random1 = randint(1,36)
	if(random1 == 1):
		newChar = "a"
	elif(random1 == 2):
		newChar = "b"
	elif(random1 == 3):
		newChar = "c"
	elif(random1 == 4):
		newChar = "d"
	elif(random1 == 5):
		newChar = "e"
	elif(random1 == 6):
		newChar = "f"
	elif(random1 == 7):
		newChar = "g"
	elif(random1 == 8):
		newChar = "h"
	elif(random1 == 9):
		newChar = "i"
	elif(random1 == 10):
		newChar = "j"
	elif(random1 == 11):
		newChar = "k"
	elif(random1 == 12):
		newChar = "l"
	elif(random1 == 13):
		newChar = "m"
	elif(random1 == 14):
		newChar = "n"
	elif(random1 == 15):
		newChar = "o"
	elif(random1 == 16):
		newChar = "p"
	elif(random1 == 17):
		newChar = "q"
	elif(random1 == 18):
		newChar = "r"
	elif(random1 == 19):
		newChar = "s"
	elif(random1 == 20):
		newChar = "t"
	elif(random1 == 21):
		newChar = "u"
	elif(random1 == 22):
		newChar = "v"
	elif(random1 == 23):
		newChar = "w"
	elif(random1 == 24):
		newChar = "x"
	elif(random1 == 25):
		newChar = "y"
	elif(random1 == 26):
		newChar = "z"
	elif(random1 == 27):
		newChar = "0"
	elif(random1 == 28):
		newChar = "1"
	elif(random1 == 29):
		newChar = "2"
	elif(random1 == 30):
		newChar = "3"
	elif(random1 == 31):
		newChar = "4"
	elif(random1 == 32):
		newChar = "5"
	elif(random1 == 33):
		newChar = "6"
	elif(random1 == 34):
		newChar = "7"
	elif(random1 == 35):
		newChar = "8"
	elif(random1 == 36):
		newChar = "9"
childname[random0] = newChar
childname = "".join(childname)
child = open(childname, "w")
parent = open(os.path.basename(__file__), "r")
parentString = parent.read()
random3 = randint(0,1)
random0 = abs(math.floor(randint(0,len(parentString)-1)**(1/2.5)/2 - 2))
random1 = randint(0,len(parentString)-1)
parentString = list(parentString)
newChars = []
for x in range(0, random0):
	random2 = randint(1, 57)
	if(random2 == 1):
		newChars.append("a")
	elif(random2 == 2):
		newChars.append("b")
	elif(random2 == 3):
		newChars.append("c")
	elif(random2 == 4):
		newChars.append("d")
	elif(random2 == 5):
		newChars.append("e")
	elif(random2 == 6):
		newChars.append("f")
	elif(random2 == 7):
		newChars.append("g")
	elif(random2 == 8):
		newChars.append("h")
	elif(random2 == 9):
		newChars.append("i")
	elif(random2 == 10):
		newChars.append("j")
	elif(random2 == 11):
		newChars.append("k")
	elif(random2 == 12):
		newChars.append("l")
	elif(random2 == 13):
		newChars.append("m")
	elif(random2 == 14):
		newChars.append("n")
	elif(random2 == 15):
		newChars.append("o")
	elif(random2 == 16):
		newChars.append("p")
	elif(random2 == 17):
		newChars.append("q")
	elif(random2 == 18):
		newChars.append("r")
	elif(random2 == 19):
		newChars.append("s")
	elif(random2 == 20):
		newChars.append("t")
	elif(random2 == 21):
		newChars.append("u")
	elif(random2 == 22):
		newChars.append("v")
	elif(random2 == 23):
		newChars.append("w")
	elif(random2 == 24):
		newChars.append("x")
	elif(random2 == 25):
		newChars.append("y")
	elif(random2 == 26):
		newChars.append("z")
	elif(random2 == 27):
		newChars.append("0")
	elif(random2 == 28):
		newChars.append("1")
	elif(random2 == 29):
		newChars.append("2")
	elif(random2 == 30):
		newChars.append("3")
	elif(random2 == 31):
		newChars.append("4")
	elif(random2 == 32):
		newChars.append("5")
	elif(random2 == 33):
		newChars.append("6")
	elif(random2 == 34):
		newChars.append("7")
	elif(random2 == 35):
		newChars.append("8")
	elif(random2 == 36):
		newChars.append("9")
	elif(random2 == 37):
		newChars.append("(")
	elif(random2 == 38):
		newChars.append(")")
	elif(random2 == 39):
		newChars.append("=")
	elif(random2 == 40):
		newChars.append("-")
	elif(random2 == 41):
		newChars.append("+")
	elif(random2 == 42):
		newChars.append("/")
	elif(random2 == 43):
		newChars.append("*")
	elif(random2 == 44):
		newChars.append(":")
	elif(random2 == 45):
		newChars.append("&")
	elif(random2 == 46):
		newChars.append("#")
	elif(random2 == 47):
		newChars.append("'")
	elif(random2 == 48):
		newChars.append(",")
	elif(random2 == 49):
		newChars.append("^")
	elif(random2 == 50):
		newChars.append("|")
	elif(random2 == 51):
		newChars.append('"')
	elif(random2 == 52):
		newChars.append("\n")
	elif(random2 == 53):
		newChars.append("")
	elif(random2 == 54):
		newChars.append(" ")
	elif(random2 == 55):
		newChars.append("_")
	elif(random2 == 56):
		newChars.append("~")
	elif(random2 == 57):
		newChars.append("!")
if(random3 == 0):
	for x in range(0, random0):
		if(len(newChars) != 0):
			parentString.insert(random1+x, newChars[x])
	parentString = "".join(parentString)
	print("inserted")
elif(random3 == 1):
	for x in range(0, random0):
		if(len(newChars) != 0):
			parentString[random1+x] = newChars[x]
	parentString = "".join(parentString)
	print("replaced")
print("new charset = ", newChars)
print("mutation ammount = ", random0)
print("mutation place = ", random1)
print("child = "+childname)
child.write(parentString)
os.system("start python "+childname+" 1")
os.system("start python "+os.path.basename(__file__)+" 1")