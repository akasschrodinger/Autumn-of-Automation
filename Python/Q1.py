def check_prime(n):

    f = 0

    for i in range (2, n//2 +1):
        if n%i==0 :
            f= 1
            break

    return f



def min_range(d):

    a = (10**(d-1))

    return a


def max_range(d):

    b = (10**d)

    return b



d=int(input("Enter d"))

twin_prime_list = []



for i in range ( min_range(d) , max_range(d) ):

    if check_prime(i)== 0 and check_prime(i+2)== 0:

        twin_prime_list.append((i, i+2))


with open("twin_prime_list.txt", "w") as f:

   for twin_pair in twin_prime_list:
    f.write(str(twin_pair))
    f.write("\n")



