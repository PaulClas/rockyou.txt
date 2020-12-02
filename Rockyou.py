a_file=open("rockyou_7.txt","r")
lines=a_file.readlines()
a_file.close()
new_file=open("rockyou_7numbers","w")
for line in lines:
    if line.strip("\n").isalpha()==False:
        new_file.write(line)
new_file.close()