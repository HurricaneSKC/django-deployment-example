import os

with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:

    myFile.write("Some random text\nMore rnadom text\nAnd some more")

with open("mydata2.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break

        print("Line", lineNum, " : ", line, end="")

        lineNum += 1



