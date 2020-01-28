import random

def func():
    x=random.randint(0,11)
    n=int(input('enter a no, bet 0 and 10 :'))

    if(x==n):
        print('you won')
    elif(x!=n):
        print('you lose')
    else:
        print('wrong input')
        
func()
print('better luck next time')
print("added extra line")
