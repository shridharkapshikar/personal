import os, sys, string
import csv
lst=[]   #empty list
 
def fileCount(fname):
    lineCount = 0
    wordCount = 0
    charCount = 0
    words = []
 
    #file is opened and assigned a variable
    infile = open(fname, 'r')
 
    #loop that finds the number of lines in the file
    for line in infile:
        print line.strip()
        lineCount = lineCount + 1
        word = line.split()
        words = words + word
 
    #loop that finds the number of words in the file
    for word in words:
        wordCount = wordCount + 1
        #loop that finds the number of characters in the file
        for char in word:
            charCount = charCount + 1
    #returns the variables so they can be called to the main function
    print line.strip()
    return(lineCount, wordCount, charCount)
 
def csv_reader(fname):
        csvfile = open(fname)
        csv_f = csv.reader(csvfile)
        for col in csv_f:
                print col
        print "\nNumber of column in csv file :",len(col)
        print "Number of Rows in csv file :",len(list(csv.reader(open(fname))))
 
ans = True
os.system("clear")
while ans:
    print("\n\n\t@@@@@@@@@@@@@@@@@@")
    print("\n\t\tMenu\n")
    print("\t@@@@@@@@@@@@@@@@@@")
    print("\n\t  1. Parse <filename>: ")
    print("\t  2. show info of last parsed file")
    print("\t  3. show info of all parsed files ")
    print("\t  4. del info of oldest parsed file ")
    print("\t  5, Exit/Quit")
 
    ans =raw_input("Please enter your choice(1-4)# ")
    if ans=="1":
        try:
            filename = raw_input("enter the filename :")
            if filename.endswith(".txt"):
                print"\nYou have entered TEXT file: ",filename
            elif filename.endswith(".csv"):
                print"\nYou have entered EXCEL CSV file: ",filename
 
            else:
                print("\nYou have entered wrong file extention: ",filename)
 
            lst.append(filename)
            if filename.endswith(".txt"):
                print "\nFile contents as below : "
                print "\n---------------------------"
                lineCount, wordCount, charCount = fileCount(filename)
                print "There are", lineCount, "lines in the file."
                print "There are", charCount, "characters in the file."
                print "There are", wordCount, "words in the file."
            elif filename.endswith(".csv"):
                print "\nFile contents as below : "
                print "\n---------------------------"
                csv_reader(filename)
            else:
                 print("\nYou have entered wrong file extention: ",filename)
 
 
 
#            csv_file()
        except IOError, OSError:
            print "\n\tFile cannot be opened: ",filename
 
 
    elif ans=="2":
        try:
            if len(lst) > 0:
                print("\nLast Parsed file is ")
                print lst[-1]
            else:
                print "\nNo files parsed yet: "
        except NameError:
            print("\n No Parsed file")
 
    elif ans=="3":
        try:
            if len(lst) == 0:
                print("\n No files to display")
            else:
                print "\nThe files are -->",lst
        except NameError:
            print("\n No Parsed file")
 
    elif ans=="4":
        try:
            if len(lst) == 0:
                print "\nNo files info to delete"
            else:
                print "\n Deleting info of oldest file"
                del lst
                print "\nDone...."
        except NameError:
            print("\n No Parsed file")
 
 
    elif ans=="5":
        ans = None
 
    else:
        print("\n Not valid choice Try again")
