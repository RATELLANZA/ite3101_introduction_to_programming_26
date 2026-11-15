def is_prime(x:int)->bool:
    if x< 2:
        return False
    else:
        for n in range(2, x-1)