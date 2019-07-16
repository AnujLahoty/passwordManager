import shelve
import random
import sys
import pyperclip


def passwordGenerator():
    s = "123456789kjefkjherfhio#@%*hjkhl"
    s1 = ""
    for iterator in range(10):
        s1 += s[random.randint(1, 10)]
        s1 += s[random.randint(15, 20)]
        s1 += s[random.randint(23, 26)]
    return s1


if len(sys.argv) < 2:
    print("please also enter the account name for which you want password")
    sys.exit()

reqAccountPassword = sys.argv[1]
# reqAccountPassword = input("Please enter the account name you want password for\n").lower()
flag = 0
o = shelve.open("Password.txt", writeback=True)
for i in o:
    if i == reqAccountPassword.lower():
        pyperclip.copy(o[i])
        print("Your password is copied to clipboard")

        flag = 1
if flag == 0:
    print('you do not have any account named ' + reqAccountPassword)
    print("Are you sure you want to create password for " + reqAccountPassword + "If yes press y or press n")
    answer = input()
    if answer == "y":
        print("Do you want to set it yourself or you want to set it automatically")
        print("Type 'A' for automatic else type 'S' for self")
        ch = input("\n")
        if ch == 'A':
            set1 = passwordGenerator()
        elif ch == 'S':
            set1 = input()
        else:
            print("Not valid choice")
            sys.exit(0)
        setPassword = set1
        o[reqAccountPassword] = setPassword
        pyperclip.copy(o[reqAccountPassword])
        print("Password Successfully added and copied")
o.close()
