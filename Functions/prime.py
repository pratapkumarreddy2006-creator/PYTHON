def prime(n):
        if n <= 1:
            print("Not a Prime number")
            return
        for i in range(2, n):
            if (n % i) == 0:
                print("Not a Prime number")
                break
        else:
            print("Prime number")

prime(1)