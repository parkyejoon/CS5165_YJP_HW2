## Yejoon Park
## University of Cincinnati
## Homework 2 Docker

import glob
import os
import socket
import sys

## a. list name of all the text files
f = open(r'C:\Users\YeJoon\Desktop\hw2\home\output\result.txt', 'a')
print('---------------------------------------------------------------------', file = f)
os.chdir(r'C:\Users\YeJoon\Desktop\hw2\home\data')
myFiles = glob.glob('*.txt')
print('All text files at the location: /home/data is', myFiles, file = f)
print('---------------------------------------------------------------------', file = f)
f.close()

## gtotal is grand total, maxcount is max count of words
os.chdir(r'C:\Users\YeJoon\Desktop\hw2\home\data')
gtotal = 0
maxcount = 0

## b. list and count total number of words in each text file
i = 0
while i < len(myFiles):
    file = open(myFiles[i], "rt")
    data = file.read()
    words = data.split()
    if len(words) >= maxcount:
        maxcount = len(words)
        maxfilename = myFiles[i]
    gtotal = gtotal + len(words)
    f = open(r'C:\Users\YeJoon\Desktop\hw2\home\output\result.txt', 'a')
    print('Total number of file,', myFiles[i], ', is',len(words), file = f)
    i = i+1
    f.close()

## c. print grand total
f = open(r'C:\Users\YeJoon\Desktop\hw2\home\output\result.txt', 'a')
print('---------------------------------------------------------------------', file = f)
print('Total number of words in all files, the grand total, is', gtotal, file = f)
print('---------------------------------------------------------------------', file = f)

## d. list the file name with the maximum number of words count
print('The file name of the maximum number of words is :', maxfilename, file = f)
print('It has a total of', maxcount, 'words count.', file = f)
print('---------------------------------------------------------------------', file = f)

## e. find the ip address of user's machine
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"IP Address of your machine is {ip_address}", file = f)
print('---------------------------------------------------------------------', file = f)
f.close()
## f. all the information is written and saved in the result.txt file

## g. print result.txt file on the console
f = open(r'C:\Users\YeJoon\Desktop\hw2\home\output\result.txt', 'r')
print(f.read())
f.close()



