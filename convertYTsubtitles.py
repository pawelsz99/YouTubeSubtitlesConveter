# -------------------------------------------------------------------------------
# Name:        convertYTsubtitles.py
# Purpose:     removes empty lines from txt file
#
# Author:      Pawel Sznura
#
# Created:     04/03/2021
# Copyright:   (c) Pawel Sznura 2021
# -------------------------------------------------------------------------------


def remove_newlines(fname):
    flist = open(fname).readlines()
    listtext = [s.rstrip('\n') for s in flist]
    info = ""
    for x in listtext:
        if x == "":
            info += " "
        else:
            info += x
    return info


# enter here the name of the file with the text
newText = remove_newlines("text.txt")

# name your new file
file1 = open("newText.txt", "w")
file1.write(newText)
file1.close()
