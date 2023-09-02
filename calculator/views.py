from django.shortcuts import render
from django.http import HttpResponse

def sumar(request, num1, num2):
    resultado = int(num1) + int(num2)
    return HttpResponse(f'La suma de {num1} + {num2} = {resultado}')