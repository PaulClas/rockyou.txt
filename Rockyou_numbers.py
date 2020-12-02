a_file=open("rockyou.txt","r")
lines=a_file.readlines()
a_file.close()
new_file=open("rockyou_7numbers_only.txt","w")
for line in lines:
    a_string=line.strip("\n")
    a_string_lowercase=a_string.lower()
    contains_letters=a_string_lowercase.islower()
    if len(a_string)==7 and contains_letters==False :
        new_file.write(line)
new_file.close()