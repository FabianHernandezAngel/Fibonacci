def fibbonachi(n, cache):
    if n == 0:
        print("Cache hit 0: returning 0")
        return 0
    elif n == 1:
        print("Cache hit 1: returning 1")
        return 1
    elif n in cache:
        print("Cache hit", n, ": returning ", cache[n])
        return cache[n]
    else:
        number = fibbonachi(n - 1, cache) + fibbonachi(n - 2, cache)
        cache[n] = number
        print("Cache missed: ", n, " computed value: ", number)
        return number

if __name__ == "__main__":
    print(fibbonachi(15, {}))