import time
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
option = 1
while option == 1:
    choice = input("choose which option you would like to pick ")
    if choice == ("1"):
        print("test")
        option +=1
    elif choice == ("2"):
        print("test2")
        option += 1
    elif choice == ("3"):
        print("test3")
        option += 1
    else:
        print("aw dang, mate you didint select an option please restart this aplication ")
        print("")
        print("and run it again and select an option one through three ")
        print("")