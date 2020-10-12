x=0
y=1
a=int(input("Enter limit="))
print(x,"\n",y," ")
for a in range(0,a-1):
    ans = x+y
    x=y
    y=ans
    print(ans," ")
  
