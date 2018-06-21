# cycle through each line to be output
# output words per line
# average word length


import os

with open("mydata2.txt", mode="w", encoding="utf-8") as myFile:

    myFile.write("Some random text\nMore rnadom text\nAnd some more")

with open("mydata2.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()


        if not line:
            break

        print("Line", lineNum)

        # split()
        wordList = line.split()

        # len()
        print("Number of words: ", len(wordList))

        # loop through the characters - count each word
        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        # divede char count / len word list
        avgChar = charCount/len(wordList)

        print("Ave word length : {:.2}".format(avgChar))

        lineNum += 1

