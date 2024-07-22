#Password generator

import string
import secrets
pwlen=int(input("Enter password length :"))
l=string.ascii_letters
d=string.digits
m=string.punctuation
listpw=l+d+m
pw=''
for i in range(pwlen):
    pw+=secrets.choice(listpw)
print("Generated password is",pw)