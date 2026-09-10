############################
#Code: ReadBinFile.py

#Author:Madison G Austin

#Lab assignment 10 - this code will read and display the previous script

#Example used:  python ReadBinFile.py
############################


def read_record(file, index):
    file.seek(index * 49)
    title = file.read(20).decode("ascii").strip()
    author= file.read(20).decode("ascii").strip()
    numPages= int.from_bytes(file.read(4), byteorder='little')
    price= int.from_bytes(file.read(4), byteorder='little') / 100
    available = int.from_bytes(file.read(1), byteorder='little')
    return title, author, numPages, price, available

file = open('books.bin', 'rb+')
print("initial Records:")
for i in range(10):
    print(read_record(file, i))
    
record_modify= int(input("Enter record number to modify (0-9): "))
new_title= input("Enter new title: ").ljust(20)[:20]
new_author= input("Enter new author: ").ljust(20)[:20]
new_num_pages= int(input("Enter new pages: "))
new_price= float(input("Enter new price: "))
new_available= int(input("Enter 1 if available, 0 if not: "))

file.seek(record_modify * 49)
file.write(new_title.encode('ascii'))
file.write(new_author.encode('ascii'))
file.write(new_num_pages.to_bytes(4, byteorder='little'))
file.write(int(new_price * 100).to_bytes(4, byteorder='little'))
file.write(new_available.to_bytes(1, byteorder='little'))

print("\nUpdated records: ")
file.seek(0)
for i in range(10):
    print(read_record(file, i))
file.close()