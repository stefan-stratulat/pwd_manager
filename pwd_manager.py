import random
import string
import re

#charachters to form password
letters = string.ascii_letters
number = random.randint(0,9)
special = "@$!%*#?&"

pwd = ''
#password creation

while len(pwd)<15:
        pwd = pwd + random.choice(random.choice(letters)+str(number)+random.choice(special))
print(pwd)
def validator():
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    #compiling regex
    pat = re.compile(reg)
    #searching regex
    match = re.search(pat, pwd)
    #validation
    if match:
        print("Password is valid!")
    else:
        print('Password is invalid!')

#Driver code
if __name__ == '__main__':
    validator()

