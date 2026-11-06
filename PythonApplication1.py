import time
# dont know if this is needed or not but better safe than sorry
import math
start = 1
while start == 1:
    name = input("hello welcome to my test application please state your name =p ")
    if name == (""):
        print("")
        print("you have to put a name")
        print("")
    elif name == "no":
        print(" ")
        print("gfys")
        print("")
    else:
        print(" ")
        start += 1
    print("hello nice to meet you", name , "hope you enjoy this little test of my skill so far");time.sleep(1)

print("you are gonna get a choice on what you want to do");time.sleep(0.9)
print("")
print("1st, multiply two numbers ")
print("")
print("2nd i can tell you a story =P ")
print("")
print("3rd you can guess a number from one through ten")
print("")
# probaly not the best solution for making else not skip but it works and should not cause any promblems
option = 1
while option == 1:
    choice = input("choose which option you would like to pick ")
    if choice == ("1"):
        option +=1
    elif choice == ("2"):
        option += 1
    elif choice == ("3"):
        option += 1
    else:
        print("aw dang, mate you didint select an option please restart this aplication ")
        print("")
        print("and run it again and select an option one through three ")
        print("")
n3 = 0 
answer = 0
int(answer)
# omg this took so long ): and i had to google it but no AI was used :D i hate AI
if choice == ("1"):
    n1 = int(input("select the first number "))
    print("")
    n2 = int(input("select your second number "))
    answer = n1 * n2
    print(answer); time.sleep(3)
    print("")
    print("welp thats it for this section try one of the other options :D")