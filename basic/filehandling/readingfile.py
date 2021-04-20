# opening a file by providing path and giving only read privilege
f = open("D:\\pythonproject\\basic\\data\\read.txt", "r")
# reading the file
print(f.read())
# closing file
f.close()

# opening a file by providing path and giving only appened privilege
f = open("D:\\pythonproject\\basic\\data\\read.txt", "a")
f.write(" we are appending the line")

# closing file
f.close()

# Handling exception
try:
    fw = open("D:\\pythonproject\\basic\\data\\write.txt", "x")

except:
    print(" file already exists")

# opening a file by providing path and giving only writing privilege
fw = open("D:\\pythonproject\\basic\\data\\write.txt", "w")
fw.write(" this is the new file")

# closing both the files
fw.close()
f.close()
