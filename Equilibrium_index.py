s=int(input("Enter size of the array "))
l=[int(x) for x in input("Enter the array ").strip().split(" ")]
equi=len(l)//2
#print(equi)
flag=False
gr=False
le=False

for i in range(s):
    sum1=0
    sum2=0
    
    for j in range(s):
        if j<equi :
            sum1+=l[j]
            #print(sum1)
        elif j>equi :
            sum2+=l[j]
            #print(sum2)
    if sum1<sum2:
        le=True
        if gr==True:
            break
        else:
            equi+=1
            #print("<")
            #print(equi)
    elif sum1>sum2:
        gr=True
        if le==True:
            break
        else:
            equi-=1
            #print(">")
            #print(equi)
    else:
        print("The equilibrium index is ",equi)
        #print("=")
        flag=True
        break
if flag==False:
    print("Equilibrium index doesn't exist")
