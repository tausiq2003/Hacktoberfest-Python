import numpy as np
l=[1,2,3,4,5,6,7,8,9]
print("1- This game is a two member game only")
print("2- 1st player is 'X' & 2nd player is 'O'")
print("3- The player will win if it makes 3 symbol in same row,same column or same diagonal")
def fun():
    print("\n")
    print("         |         |       ")
    print("         |         |       ")
    print("   ",l[0],"   |   ",l[1],"   |   ",l[2],"   ")
    print("         |         |       ")
    print("         |         |       ")
    print("---------------------------")
    print("         |         |       ")
    print("         |         |       ")
    print("   ",l[3],"   |   ",l[4],"   |   ",l[5],"   ")
    print("         |         |       ")
    print("         |         |       ")
    print("---------------------------")
    print("         |         |       ")
    print("         |         |       ")
    print("   ",l[6],"   |   ",l[7],"   |   ",l[8],"   ")
    print("         |         |       ")
    print("         |         |       ")
name1=input("Enter the name of 1st player")
name2=input("Enter the name of  2nd player")
fun()
i=0
while(1):
    print("Turn of 1st player")
    a=int(input("enter the position at which you want to place X"))
    if(a<1 or a>9 or l[a-1]=='X' or l[a-1]=='O'):
        print("enter the correct choice")
        break
    else:
        l[a-1]='X'
        fun()
        if((l[0]=='X' and l[1]=='X' and l[2]=='X') or (l[3]=='X' and l[4]=='X' and l[5]=='X') or (l[6]=='X' and l[7]=='X' and l[8]=='X')  or (l[0]=='X' and l[3]=='X' and l[6]=='X')or (l[1]=='X' and l[4]=='X' and l[7]=='X')or (l[2]=='X' and l[5]=='X' and l[8]=='X')or (l[0]=='X' and l[4]=='X' and l[8]=='X')or (l[2]=='X' and l[4]=='X' and l[6]=='X')):
            print("",name1,"!Win")
            break
    i=i+1
    if i==5:
        print("Match Tie!!Try Again")
        break
    print("Turn of 2nd player")
    b=int(input("enter the position in which you want to place 0"))
    if(b<1 or b>9 or l[b-1]=='X' or l[b-1]=='O'):
        print("enter the correct choice")
        break
    else:
        l[b-1]='O'
        fun()
        if((l[0]=='O' and l[1]=='O' and l[2]=='O') or (l[3]=='O' and l[4]=='O' and l[5]=='O') or (l[6]=='O' and l[7]=='O' and l[8]=='O')  or (l[0]=='O' and l[3]=='O' and l[6]=='O')or (l[1]=='O' and l[4]=='O' and l[7]=='O')or (l[2]=='O' and l[5]=='O' and l[8]=='O')or (l[0]=='O' and l[4]=='O' and l[8]=='O')or (l[2]=='O' and l[4]=='O' and l[6]=='O')):
            print("",name2,"!Win")
            break
