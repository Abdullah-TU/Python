# procedure 1

def factorial(n):
    facto = 1
    for i in range(n):
        facto = facto* (i + 1)
    return facto

ask=int(input('Enter a number: '))
print('Factorial of {}! is {}'.format(ask, factorial(ask)))


# procedure 2

def factorial(n):
    for i in range(n + 1):
        if n == 0:
            facto = 1
            return facto

        else:
            facto = 1
            for i in range(1, n + 1):
                facto = facto * i
            return facto


ask = int(input('Enter a number: '))
print('Factorial of {}! is {}'.format(ask, factorial(ask)))
