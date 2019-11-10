import py_compile
import time
import os
type = input("which type\n")
layers = input("how many layers\n")
if(layers == "1"):
	while(True):
		goodStrings = []
		for x in range(0, 36):
			if(x == 0):
				string = ""
			if(x == 1):
				string = "a"
			if(x == 2):
				string = "b"
			if(x == 3):
				string = "c"
			if(x == 4):
				string = "d"
			if(x == 5):
				string = "e"
			if(x == 6):
				string = "f"
			if(x == 7):
				string = "g"
			if(x == 8):
				string = "h"
			if(x == 9):
				string = "i"
			if(x == 10):
				string = "j"
			if(x == 11):
				string = "k"
			if(x == 12):
				string = "l"
			if(x == 13):
				string = "m"
			if(x == 14):
				string = "n"
			if(x == 15):
				string = "o"
			if(x == 16):
				string = "p"
			if(x == 17):
				string = "q"
			if(x == 18):
				string = "r"
			if(x == 19):
				string = "s"
			if(x == 20):
				string = "t"
			if(x == 21):
				string = "u"
			if(x == 22):
				string = "v"
			if(x == 23):
				string = "w"
			if(x == 24):
				string = "x"
			if(x == 25):
				string = "y"
			if(x == 26):
				string = "z"
			if(x == 27):
				string = "0"
			if(x == 28):
				string = "1"
			if(x == 29):
				string = "2"
			if(x == 30):
				string = "3"
			if(x == 31):
				string = "4"
			if(x == 32):
				string = "5"
			if(x == 33):
				string = "6"
			if(x == 34):
				string = "7"
			if(x == 35):
				string = "8"
			if(x == 36):
				string = "9"
			if(os.path.exists(type+"/"+string+".py")):
				if(py_compile.compile(type+"/"+string+".py") != None):
					goodStrings.append(string)
				else:
					os.remove(type+"/"+string+".py")
		os.system('cls')
		for x in range(0, len(goodStrings)):
			print(goodStrings[x]+" - is viable")
		time.sleep(1)
if(layers == "2"):
	while(True):
		goodStrings = []
		string = ["",""]
		for x in range(0, 37):
			if(x == 0):
				string[0] = ""
			if(x == 1):
				string[0] = "a"
			if(x == 2):
				string[0] = "b"
			if(x == 3):
				string[0] = "c"
			if(x == 4):
				string[0] = "d"
			if(x == 5):
				string[0] = "e"
			if(x == 6):
				string[0] = "f"
			if(x == 7):
				string[0] = "g"
			if(x == 8):
				string[0] = "h"
			if(x == 9):
				string[0] = "i"
			if(x == 10):
				string[0] = "j"
			if(x == 11):
				string[0] = "k"
			if(x == 12):
				string[0] = "l"
			if(x == 13):
				string[0] = "m"
			if(x == 14):
				string[0] = "n"
			if(x == 15):
				string[0] = "o"
			if(x == 16):
				string[0] = "p"
			if(x == 17):
				string[0] = "q"
			if(x == 18):
				string[0] = "r"
			if(x == 19):
				string[0] = "s"
			if(x == 20):
				string[0] = "t"
			if(x == 21):
				string[0] = "u"
			if(x == 22):
				string[0] = "v"
			if(x == 23):
				string[0] = "w"
			if(x == 24):
				string[0] = "x"
			if(x == 25):
				string[0] = "y"
			if(x == 26):
				string[0] = "z"
			if(x == 27):
				string[0] = "0"
			if(x == 28):
				string[0] = "1"
			if(x == 29):
				string[0] = "2"
			if(x == 30):
				string[0] = "3"
			if(x == 31):
				string[0] = "4"
			if(x == 32):
				string[0] = "5"
			if(x == 33):
				string[0] = "6"
			if(x == 34):
				string[0] = "7"
			if(x == 35):
				string[0] = "8"
			if(x == 36):
				string[0] = "9"
			for y in range(0, 37):
				if(y == 0):
					string[1] = ""
				if(y == 1):
					string[1] = "a"
				if(y == 2):
					string[1] = "b"
				if(y == 3):
					string[1] = "c"
				if(y == 4):
					string[1] = "d"
				if(y == 5):
					string[1] = "e"
				if(y == 6):
					string[1] = "f"
				if(y == 7):
					string[1] = "g"
				if(y == 8):
					string[1] = "h"
				if(y == 9):
					string[1] = "i"
				if(y == 10):
					string[1] = "j"
				if(y == 11):
					string[1] = "k"
				if(y == 12):
					string[1] = "l"
				if(y == 13):
					string[1] = "m"
				if(y == 14):
					string[1] = "n"
				if(y == 15):
					string[1] = "o"
				if(y == 16):
					string[1] = "p"
				if(y == 17):
					string[1] = "q"
				if(y == 18):
					string[1] = "r"
				if(y == 19):
					string[1] = "s"
				if(y == 20):
					string[1] = "t"
				if(y == 21):
					string[1] = "u"
				if(y == 22):
					string[1] = "v"
				if(y == 23):
					string[1] = "w"
				if(y == 24):
					string[1] = "x"
				if(y == 25):
					string[1] = "y"
				if(y == 26):
					string[1] = "z"
				if(y == 27):
					string[1] = "0"
				if(y == 28):
					string[1] = "1"
				if(y == 29):
					string[1] = "2"
				if(y == 30):
					string[1] = "3"
				if(y == 31):
					string[1] = "4"
				if(y == 32):
					string[1] = "5"
				if(y == 33):
					string[1] = "6"
				if(y == 34):
					string[1] = "7"
				if(y == 35):
					string[1] = "8"
				if(y == 36):
					string[1] = "9"
				if(os.path.exists(type+"/"+string[0]+string[1]+".py")):
					if(py_compile.compile(type+"/"+string[0]+string[1]+".py") != None):
						goodStrings.append(string[0]+string[1])
					else:
						os.remove(type+"/"+string[0]+string[1]+".py")
		os.system('cls')
		for x in range(0, len(goodStrings)):
			print(goodStrings[x]+" - is viable")
		time.sleep(2)