#file handling
filename = "spectrum.txt"
myFile=open(filename) #will open specified file with specified mode default made is results
print("Mode : ",myFile.mode)
print ( myFile.read())
myFile.close()#will close file
