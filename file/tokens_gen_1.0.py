# This script generate a list of poor random tokens (1000)
# The encoded base64 token patterns is: 
#   b64({a random string, 10 chars length created randomly from 5 letters (a,m,e,l,y)} + {UTC date.time in seconds})
# The logic of this token generation was found in a real J2EE app as session token. Here a new token creation is delayed of one second
# to have a bit more of randomness, the delay was not implemented in the real algorithm.


import time
import random
import string
import base64
import sys

def print_progress_bar(index, total, label):
    n_bar = 90  # Progress bar width
    progress = index / total
    sys.stdout.write('\r')
    sys.stdout.write(f"[{'*' * int(n_bar * progress):{n_bar}s}] {int(100 * progress)}%  {label}")
    sys.stdout.flush()

f1 = open("tokensB64.txt","a")
f2 = open("tokens.txt","a")

lent = 1000

for i in range(lent):

    letters = ['a','m','e','l','y'] #string.ascii_lowercase
    ts = round(time.time())
    inc = (''.join(random.choice(letters) for i in range(10)))
    
    tkpln = inc + str(ts)
    f2.write(tkpln + "\n")
    
    tkb64 = base64.b64encode(tkpln.encode('ascii')).decode('ascii')
    f1.write(tkb64 + "\n")
    
    print_progress_bar(i, lent, "progress")
    
    time.sleep(1)

print_progress_bar(lent, lent, "DONE    ")
    
f1.close()
f2.close()