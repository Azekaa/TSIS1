def isPrime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True
    
numbers = list(map(int, input("Enter a list: ").split()))

primeNumbers = list(filter(lambda x: isPrime(x), numbers))

print("Prime numbers in your list:", primeNumbers)