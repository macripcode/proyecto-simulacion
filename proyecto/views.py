from django.shortcuts import render
from .forms import InputForm
from proyecto.sistema import *


def handle_input(tiempo_llegadas, desviacion_tiempo, numero_reinas):
    return 0


def public_page(request):
    output_file = 'vacio'

    if request.method == 'POST':
        input_form = InputForm(request.POST)

        if input_form.is_valid():
            numero_retadores = input_form.data['numero_retadores']
            tiempo_llegadas = input_form.data['tiempo_llegadas']
            desviacion_tiempo = input_form.data['desviacion_tiempo']
            numero_reinas = input_form.data['numero_reinas']
            output_file = handle_input(tiempo_llegadas,desviacion_tiempo,numero_reinas)

            print("El numero retadores es: "+str(numero_retadores))
            print("El tiempo es:     "+str(tiempo_llegadas))
            print("La desviacion es: "+str(desviacion_tiempo))
            print("Numero de reinas: "+str(numero_reinas))


            # def __init__(self, num_retadores, numero_reinas, tiempo_entre_llegadas, desv_tiempo_llegadas):
            nr = Simulacion(int(numero_retadores), int(numero_reinas), int(tiempo_llegadas),int(desviacion_tiempo))
            nr.generarSimulacion()
            nr.generarEstadisticasExcel()

            #hacer indicador de terminar



    else:
        input_form = InputForm()

    context = {
        'input_form': input_form,
        'output_file': output_file,
    }

    return render(request, 'home.html', context)
