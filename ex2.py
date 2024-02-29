# Escriba un programa que obtenga el primer y ultimo valor de una lista
def getFirstAndLastFrom(myList):
    return myList[0], myList[-1]


def getFibonacciNumbers(value):
    fibonacciNumbers = [1, 1]
    newValue = 2
    while newValue <= value:
        newValue = fibonacciNumbers[-2] + fibonacciNumbers[-1]
        if newValue >= value:
            break
        fibonacciNumbers.append(newValue)
    return fibonacciNumbers

result = getFibonacciNumbers(0)
print(result)
