import sys

play = ["가위", "바위", "보"]
man1 = str(input())
man2 = str(input())

if man1 == "가위" :
    if man2 == "가위" :
        print("Result: Draw")
    elif man2 == "바위" :
        print("Result : Man2 Win!")
    else :
        print("Result : Man1 Win!")
elif man1 == "바위" :
    if man2 == "바위" :
        print("Result: Draw")
    elif man2 == "보" :
        print("Result : Man2 Win!")
    else :
        print("Result : Man1 Win!")
elif man1 =="보":
    if man2 == "보" :
        print("Result: Draw")
    elif man2 == "가위" :
        print("Result : Man2 Win!")
    else :
        print("Result : Man1 Win!")
