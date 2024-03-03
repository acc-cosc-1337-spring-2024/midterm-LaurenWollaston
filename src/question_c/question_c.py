import time
def get_random_number():
    val = int(time.time()*1000)
    a = 255
    c = 1250
    m = 2**8
    val = (a * val + c)%m
    return(val%5)+1