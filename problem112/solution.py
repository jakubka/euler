import itertools

def isBouncy(number):
    def getDigits(n):
        while n:
            yield n % 10
            n //= 10

    isDecreasing, isIncreasing = True, True

    digits = getDigits(number)
    previousDigit = next(digits)

    for currentDigit in digits:
        if currentDigit > previousDigit:
            isDecreasing = False
        elif currentDigit < previousDigit:
            isIncreasing = False

        if isDecreasing is False and isIncreasing is False:
            return True

        previousDigit = currentDigit

    return False

def calculateResult():
    totalBouncy = 0
    for number in itertools.count(1):
        if isBouncy(number):
            totalBouncy += 1

        if totalBouncy * 100 == number * 99:
            return number

result = calculateResult()

print("Result: {0}".format(result))