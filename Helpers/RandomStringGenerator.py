import string
import random

def randomString(n = None):
    if n == None:
        n = random.randint(1,20)
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))
