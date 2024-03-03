def test_config():
    return True

def is_prime(int):
    if int != 1 and int != -1:
        if int <= 0:
            int = abs(int)
        for i in range (2, int):
            if int%i==0:
                return(False)
        return(True)
    else:
        return(False)

