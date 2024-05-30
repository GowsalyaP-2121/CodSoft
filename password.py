import random 
import string

def password(x):
    k=''
    passw= string.ascii_letters+string.digits+string.punctuation
    return k.join(random.choice(passw) for _ in range(x))

l=int(input("Enter desired length for your password:    "))
print("Generated password: ",password(l))
