def fibonacci(n):

 a, b = 0, 1


 while a < n:

   yield a

   a, b = b, a + b


def conta_fino_a(numero_massimo):


    numero = 1


    while numero <= numero_massimo:

        yield numero

        numero = numero + 1