import time
myfile = open("C:\\Users\\Spenc\\pythonStuff\\pythonScripts\\dirstTxtFile.txt", "a")
myfile.writelines(["First write attempt", "Let's see /n", "Yeah!"])
myfile.write("/n New line baby!")


#print(myfile.readlines())
#print(myfile.readlines())
#myfile.seek(0)
#print(myfile.readlines())
myfile.close

time.sleep(2)

myfile2 = open("C:\\Users\\Spenc\\pythonStuff\\pythonScripts\\dirstTxtFile.txt")
print(myfile2.readlines())
myfile2.close