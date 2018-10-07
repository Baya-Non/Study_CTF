import os
import sys

args = sys.argv

dic = open("list.txt","r")
passwd_list=dic.read().split("\n")
print("search")
for passwd in passwd_list:
    if len(passwd) == 0:
        print("empty")
    else:
        result=os.system('unzip -P ' + passwd + ' ' + "mondai1.zip")
        if result == 0:
            print("password is found!!! ->",passwd)
            sys.exit()
print("password is not found")