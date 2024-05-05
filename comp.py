import os
ifile=input("enter source file")
file1=open(ifile,"r")
ofile=input("enter name of output file")
file2=open(ofile,"w")
count=0
command=[]
while True:
    count += 1
 
    # Get next line from file
    line = file1.readline()
    command.append(line)
    # if line is empty
    # end of file is reached
    if not line:
        break
for item in command:
    if item=="init":
        file2.write("#include <stdio.h>\n\nint main(){")
    if item=="put":
        toprint=next(command)
        file2.write("   printf(",toprint,");")
    if item=="end":
        file2.write("    return 0;\n}")