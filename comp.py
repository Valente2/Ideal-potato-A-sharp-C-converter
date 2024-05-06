import os
ifile=input("enter source file name")
file1=open(ifile,"r")
ofile=input("enter name of output file")
file2=open(ofile,"a")
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
        continue
    if item=="put":
        toprint=next(command)
        file2.write("   printf(",toprint,");")
        continue
    if item=="end":
        file2.write("   return 0;\n}")
        continue
    if item=="int":
        name=next(command)
        value=next(command)
        file2.write("   int ")