# Programa para obtención de números primos y conjetura de Goldbach
# Conjetura Goldbach dice que un número par mayor a 2 puede ser representado como la suma de 2 primos
import math


def isEven(value):
    if value % 2 == 0:
        return True


def isPrime(value):
    result = False
    if value > 1:
        for i in range(2, int(round(value / 2)) + 1):
            if (value % i) == 0:
                result = False
                break
            else:
                result = True
    return result


def getPrimeNumbers(value):
    primeNumbers = []
    numbersToCheck = range(2, value)
    for num in numbersToCheck:
        if isPrime(num):
            primeNumbers.append(num)
    return primeNumbers


def getGoldbachConjeture(primeNumbers, value):
    goldbachConjeture = []
    if isEven(value):
        for num1 in primeNumbers:
            for num2 in primeNumbers:
                if num1 + num2 == value:
                    goldbachConjeture.append([num1, num2])
    else:
        print("Valor no es par")
    return goldbachConjeture



value = int(input("Ingrese un numero entero: "))
primeNumbers = getPrimeNumbers(value)
print("numeros primos: " + str(primeNumbers))

goldbachConjeture = getGoldbachConjeture(primeNumbers,value)
print("conjetura Goldbach: " + str(goldbachConjeture))
