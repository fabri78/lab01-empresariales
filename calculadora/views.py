from django.http import HttpResponse

def sumar(request, num1, num2):
    resultado = num1 + num2
    return HttpResponse(f'La suma de {num1} + {num2} = {resultado}')