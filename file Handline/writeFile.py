from argparse import FileType


filename = "myfile.txt"
file_txt ="Hello, welcome how are you \n this is new line for testing"
#writing file code start ---
mytxtfile = open(filename,"w")
mytxtfile.write(file_txt)
mytxtfile.close()
print("file has been created")

