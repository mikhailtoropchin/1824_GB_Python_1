def factorial(number):
    result = 1
    for x in range(1, number + 1):
        result = result * x
    print(result)

factorial(5)