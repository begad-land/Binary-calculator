from django.shortcuts import render
from django.views import View
from .forms import BinaryForm

class Main(View):
    def get(self , request):
        form = BinaryForm()
        context = {'form' : form}
        return render(request , 'main.html' , context)
    
    def post(self , request):
        form = BinaryForm(request.POST)
        context = {}

        if form.is_valid():
            operation = form.cleaned_data['operation']
            number = form.cleaned_data['number']


        if operation == 'B':
            result = binary_to_decimal(number)
            context = {"form" : form , 'result' : result}
        
        elif operation == 'D':
            result = decimal_to_binary(number)
            context = {"form" : form , 'result' : result}

        return render(request , 'main.html' , context)


        


def binary_to_decimal(binary):
    if len(binary) < 7:
        for i in range(7 - len(binary)):
            binary+='0'


    numbers = [128 , 64 , 32 , 16 , 8 , 4 , 2 , 1]
    decimal = 0
    for idx, digit in enumerate(binary):
        if digit == '1':
            decimal += numbers[idx]
    return decimal


def decimal_to_binary(decimal):
    numbers = [128 , 64 , 32 , 16 , 8 , 4 , 2 , 1]
    binary = ''
    decimal = int(decimal)
    
    for number in numbers:
        if decimal >= number:
            decimal -= number
            binary+='1'
        else:
            binary+='0'
    return binary


        