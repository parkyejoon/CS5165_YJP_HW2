# CS5165_YJP_HW2

with download entire file from github.
---------------------------------------
1. add entire folder "hw2_yjp" to the 
   > C:\Windows\System32\hw2_yjp

2. open windows power shell as an admin

3. move to the hw2_yjp repository by command
   > "cd hw2_yjp"

4. docker build -t hw2_yjp:1.0 .
   > build the image

5. docker run -p 80:80 hw2_yjp:1.0
   > run the image by container

6. the output will be saved and printed.
---------------------------------------

without download entire file from github
---------------------------------------
1. just enter the command below!
   > docker run -p 80:80 yejoonpark/hw2_yjp:latest
---------------------------------------

the output will look like below
```
PS C:\WINDOWS\system32\hw2_yjp> docker run -p 80:80 hw2_yjp:1.0
---------------------------------------------------------------------
All text files at the location: \home\data is ['3.txt', '2.txt', '1.txt']
---------------------------------------------------------------------
Total number of file, 3.txt , is 11
Total number of file, 2.txt , is 3
Total number of file, 1.txt , is 8
---------------------------------------------------------------------
Total number of words in all files, the grand total, is 22
---------------------------------------------------------------------
The file name of the maximum number of words is : 3.txt
It has a total of 11 words count.
---------------------------------------------------------------------
IP Address of your machine is 172.17.0.2
---------------------------------------------------------------------
```
