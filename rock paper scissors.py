import random

i=1
user=0
com=0
k=['rock','paper','scissors']


while i==1:
    inp=input("Choose rock,paper or scissors: ")
    comp=random.choice(k)
    if inp==comp:
        print("User choice: ",inp,"\n","Computer's choice: ",comp,sep='')
        print("It's a tie")
        user+=1
        com+=1
    elif inp=='rock' and comp=='scissors':
        print("User choice: ",inp,"\n","Computer's choice: ",comp,sep='')
        print("User wins")
        user+=1
    elif inp=='scissors' and comp=='paper':
        print("User choice: ",inp,"\n","Computer's choice: ",comp,sep='')
        print("User wins")
        user+=1
    elif inp=='paper' and comp=='rock':
        print("User choice: ",inp,"\n","Computer's choice: ",comp,sep='')
        print("User wins")
        user+=1
    elif inp=='rock' and comp=='paper':
        print("User choice: ",inp,"\n","Computer's choice: ",comp,sep='')
        print("User loses")
        com+=1
    elif inp=='paper' and comp=='scissors':
        print("User choice: ",inp,"\n","Computer's choice: ",comp,sep='')
        print("User loses")
        com+=1
    elif inp=='scissors' and comp=='rock':
        print("User choice: ",inp,"\n","Computer's choice: ",comp,sep='')
        print("User loses")
        com+=1
    else:
        break
    print("you can continue you game or If you want to end this game,then juzt print 'end'")
    
print("scores: User:",user,"  ","computer:",com,sep='')
