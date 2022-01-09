import string
import subprocess as sp 

from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print (password)
sp.run("pbcopy", universal_newlines=True, input=password)
print ("Password copied to clipboard")