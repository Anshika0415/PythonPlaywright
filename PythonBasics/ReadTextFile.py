file=open("txtFile")  #always close file after opening it
#print(file.read(5))
# print(file.readline())
# print(file.readline())
# print(file.readlines()) #space is counted as character
# #readlines will add each line to list
line=file.readline()
while line!= "":
    print(line)
    line=file.readline()
file.close()

# with open("txtFile", 'r') as file:
#     lines = file.readlines()
#
# # Write all lines in reverse order (once) 'a' stands for append
# with open("txtFile", 'a') as file:
#     for item in reversed(lines):
#         file.write(item)
#
# # Now read and print the reversed file
# with open("txtFile", 'r') as file:
#     for item in file.readlines():
#         print(item)
