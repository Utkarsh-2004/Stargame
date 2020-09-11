i=int(input('pls enter an integer: '))
n=int(input('pls enter 0 or 1: '))
if n==1:
    for num in range(0,i+1):
        print('*'* num)
elif n==0:
    for num in range(i+1,0,-1):
        print('*'* num)

