a=int(input())
for i in range(0,a):
    if(i==0 or i==a-1):
        print("* "*a)
    else:
        print("* "+("  "*(a-2))+"*")
