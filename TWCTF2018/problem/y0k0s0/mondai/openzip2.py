import os
import sys

args = sys.argv

dic = open(args[1],"r")
passwd_list=dic.read().split("\n")

for passwd in passwd_list:
    if len(passwd) == 0:
        print("empty")
    else:
        result=os.system('unzip -P ' + passwd + ' ' + args[2])
        if result == 0:
            print("password is found!!! ->",passwd)
            sys.exit()
print("password is not found")