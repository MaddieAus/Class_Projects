############################
#Code: CreateBinFile.py

#Author:Madison G Austin

#Lab assignment 10 - we are making a script that is a binary file that records 10 books

#Example used:  python CreateBinFile.py
############################


title= ['Title1', 'Title2', 'Title3', 'Title4', 'Title5', 'Title6', 'Title7', 'Title8', 'Title9', 'Title10']
author= ['Author1', 'Author2', 'Author3', 'Author4', 'Author5', 'Author6', 'Author7', 'Author8', 'Author9', 'Author10']
numPages= [100,200,300,400,500,600,700,800,900,1000]
price= [5.00,10.00,13.00,15.00,17.00,20.00,25.00,30.00,35.00,40.00]
available= [1,0,1,0,1,0,1,0,1,0]



file = open('books.bin', 'wb')
for i in range(10):
    file.write(title[i].ljust(20).encode("ascii"))
    file.write(author[i].ljust(20).encode("ascii"))
    file.write(numPages[i].to_bytes(4, byteorder='little'))
    file.write(int(price[i] * 100).to_bytes(4, byteorder='little'))
    file.write(available[i].to_bytes(1, byteorder='little'))
file.close()