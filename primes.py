# third parameter refers to the output of the function
# if true, only returns boolean, otherwise returns more descriptive text
def isPrime(num, divisibleChecker, isBool):
    num = int(num)
    while True:
        if (num % divisibleChecker == 0):
            return "Prime not found! It is divisible by: " + str(divisibleChecker) if not isBool else False
        else:
            if divisibleChecker < num - 1:
                divisibleChecker += 1
            else:
                return "Prime found!" if not isBool else True


number = input("Input a number to check if it is prime...")

print(isPrime(number, 2, False))
