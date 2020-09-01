def isPrime(number):
    for i in range(2, primenum):
        if (primenum % i) == 0:
            number = False
            print("Your number is not a prime number")
            break
    else:
        print("Your number is a prime number")
            

primenum = int(input("type any number to check if is prime: "))
isPrime(primenum)