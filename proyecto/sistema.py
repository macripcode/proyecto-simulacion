#!/usr/bin/python
import random as r
from proyecto import solucion_n_reinas as snr
# MODULOS ADICIONA
# pip install XlsxWriter
# pip install pyPDF2
import xlsxwriter as xlsw
# from PyPDF2 import PdfFileWriter as pdfw, PdfFileReader as pdfr
from PyPDF2 import PdfFileWriter, PdfFileReader


class Retador:
    """Representa cada uno de los jugadores que retan al maestro.
    La propiedad id es compartida por todas las instancias de objeto, de modo que cada vez
    que se cree uno nuevo su id será el anterior incrementado en 1."""
    id = 0

    def __init__(self, tiempo_llegada,  tiempo_tarda, tiempo_salida, id=None):
        if not id is None:
            Retador.id += 1
            self.id = Retador.id
        else:
            self.id = 0
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_tarda = tiempo_tarda
        self.tiempo_salida = tiempo_salida


class Evento:
    """Representa cada uno de los eventos que se presentan en la simulación.
    @param tiempo_ocurrencia: Indica el momento en que se presenta el evento
    @param entidad:  Es la entidad que genera el evento, en el caso del proyecto NReinas, corresponde al retador.
    @param tipo: Indica si el evento que se presenta es una entrada o una salida."""

    def __init__(self, tiempo_ocurrencia, tipo, entidad):
        self.tiempo_ocurrencia = tiempo_ocurrencia
        self.tipo = tipo
        self.entidad = entidad


class Simulacion:
    """Representa cada uno de los eventos que se presentan en la simulación.
    @param lef: Lista de eventos futuros
    @param id_retador:  Dado que todos los están realcionados con un retador, este parámetro indica el retador involucrado en el evento
    @param tipo: Indica si el evento que se presenta es una entrada o una salida."""

    list_retadores = []
    lef = []
    historico_eventos = []
    reloj = 0
    atendidos = 0
    cola = 0
    cola_max = 0
    maestro_ocupado = False

    def __init__(self, num_retadores, numero_reinas, tiempo_entre_llegadas, desv_tiempo_llegadas):
        self.num_retadores = num_retadores
        self.numero_reinas = numero_reinas
        self.tiempo_entre_llegadas = tiempo_entre_llegadas
        self.desv_tiempo_llegadas = desv_tiempo_llegadas

    def generarLLegada(self,  evento):
        # Si el maestro está ocupado, se incrementa la cola, actualiza la cola máxima (si el nuevo valor de la cola es mayor), y se actualiza la ista de eventos futuros (lef)
        if self.maestro_ocupado:
            self.cola += 1
            self.cola_max = max(self.cola, self.cola_max)
            #self.actualizarLef(evento,  False)
        else:
            # Si el maestro está libre, se ocupa para simular la atención a un retador, se verifica que el reloj se mayor que 0 para ignore el evento previo al primer retador
            self.maestro_ocupado = True
            #self.actualizarLef(evento,  False)
            # if self.reloj > 0:
            #     self.generarSimulacion()
            #     # evento_salida = Evento(
            #     #     evento.entidad.tiempo_salida, "S", evento.entidad)
            # self.generarSalida(evento_salida)
        self.list_retadores.append(evento.entidad)

    def generarSalida(self,  evento):
        if self.cola > 0:
            self.cola -= 1
            self.actualizarLef(evento, False)
        self.atendidos += 1
        if self.cola == 0:
            self.actualizarLef(evento,  False)
            self.maestro_ocupado = False

    def resolverLasVegas(self):
        iteraciones = r.randint(10, 100)
        return iteraciones

    def resolverDeterministica(self):
        iteraciones = r.randint(10, 100)
        return iteraciones

    def generarSolucion(self, numero_reinas):
        # Se escoge el algoritmo con el que se resolverá el problema Nreinas con 50% de probabilidad para las vegs y 50% para deterministico
        exito = False
        solucion = []
        n_iter_n_queens = 0
        algoritmo = r.randint(0, 1)
        if algoritmo == 0:
            return snr.maestro_n_queen_vegas(numero_reinas, exito, solucion, n_iter_n_queens)
        else:
            return snr.n_queens(numero_reinas, n_iter_n_queens)

    def generarSimulacion(self):
        if not self.num_retadores == len(self.list_retadores):
            min_tiempo_netre_llegadas = self.tiempo_entre_llegadas-self.desv_tiempo_llegadas
            max_tiempo_netre_llegadas = self.tiempo_entre_llegadas+self.desv_tiempo_llegadas
            tiempo_entre_llegadas = r.randint(
                min_tiempo_netre_llegadas, max_tiempo_netre_llegadas)
            # El número de iteraciones que toma calcular la solución equivele al tiempo que tarda le mastro
            tiempo_tarda = self.generarSolucion(self.numero_reinas)
            # El timepo de llegada de cada retador es la suma entre el tiempo entre llegadas aleatorio y el tiempo de llegada del retador anterior, excepto el primero cuyo tiempo de llegada es igual al tiempo entre llegadas generado aleatoriamente.
            if Retador.id > 0:
                tiempo_llegada = self.list_retadores[-1].tiempo_llegada + \
                    tiempo_entre_llegadas
                timepo_salida = max(self.list_retadores[-1].tiempo_salida, tiempo_llegada) + \
                    tiempo_tarda
            else:
                tiempo_llegada = tiempo_entre_llegadas
                timepo_salida = tiempo_llegada + tiempo_tarda

            retador = Retador( tiempo_llegada, tiempo_tarda, timepo_salida,0)
            # Antes de generar un evento de llegada, este es agregado a la lista de eventos futuros
            evento_futuro = Evento(tiempo_llegada,  "L", retador)
            self.actualizarLef(evento_futuro,  True)

            # Generar una llegada en el tiempo 0 indicando como eventos futuros la llegada y salida del primer retador
            if self.reloj == 0:
                evento_ocurrido = Evento(
                    self.reloj,  "L", Retador(0, 0, 0, None))
                self.actualizarHistoricoEventos(evento_ocurrido)

            self.generarLLegada(evento_futuro)
            self.actualizarLef(self.lef[0],  False)
            self.generarSimulacion()
        elif len(self.lef) == 0:
            return
        else:
            self.generarSalida(self.lef[0])
            self.generarSimulacion()

    def actualizarLef(self, evento,  es_futuro):
        """Representa cada uno de los eventos que se presentan en la simulación.
        @param evento_ocurrido: Representa el último evento que se ha presentado en la simulación."""
        # Si es un evento ocurrido, se borra de la lista de eventos futuros y se actualiza el histórico de eventos ocurridos.
        if not es_futuro:
            # Se actualiza el reloj para la ocurrencia del proximo evento
            self.reloj = self.lef[0].tiempo_ocurrencia
            self.lef.pop(0)
            self.actualizarHistoricoEventos(evento)
        else:
            # Si es un evento futuro, si el es una llegada, se debe buscar la posición correcta donde insertarlo de acuerdo al tiempo en que ocurrirá, esto sería, antes del primer evento con tiempo de ocurrencia mayor que el suyo, adicionalmente, se debe agregar una salida como evento futuro para el reador que llega.
            if evento.tipo == "L":
                for evento_aux in self.lef:
                    if evento_aux.tiempo_ocurrencia > evento.tiempo_ocurrencia:
                        indice = self.lef.index(evento_aux)
                        self.lef.insert(indice, evento)
                        break
                # Si no se encontró ningún evento futuro con tiempo de ocurrencia mayor qu e el actual, el evento se agrega al final de la lista de eventos futuros.
                if evento not in self.lef:
                    self.lef.append(evento)
                # Se agrega un evento futuro de salida usando como tiempo de ocurrencia el tiempo de salida del retador
                evento_salida = Evento(
                    evento.entidad.tiempo_salida, "S", evento.entidad)
                self.lef.append(evento_salida)
            # Si no es una salido, sólo se agrega a la lista de eventos futuros
            else:
                self.lef.append(evento)

    def actualizarHistoricoEventos(self, evento_ocurrido):
        registro = []
        lef_actual = self.lef[:]
        cola_actual = self.cola
        cola_max_actual = self.cola_max
        atendidos_actual = self.atendidos
        estado_servidor = self.maestro_ocupado
        registro.append(evento_ocurrido)  # 0
        registro.append(lef_actual)  # 1
        registro.append(cola_actual)  # 2
        registro.append(cola_max_actual)  # 3
        registro.append(atendidos_actual)  # 4
        registro.append(estado_servidor)  # 5
        self.historico_eventos.append(registro)  # 6

    def generarEstadisticasExcel(self):
        workbook = xlsw.Workbook('static/EstadisticasNReinas.xlsx')
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        worksheet.set_row(0, 18, bold)
        # Escribir encabezado
        fila = 1
        worksheet.write(fila, 0, "ID Retador")
        worksheet.write(fila, 1, "Reloj")
        worksheet.write(fila, 2, "Evento Actual")
        worksheet.write(fila, 3, "Atendidos")
        worksheet.write(fila, 4, "Cola")
        worksheet.write(fila, 5, "Cola Máxima")
        worksheet.write(fila, 6, "Servidor\n ocupado")
        worksheet.write(fila, 7, "Hora de llegada")
        worksheet.write(fila, 8, "Tiempo servicio")
        worksheet.write(fila, 9, "Hora de salida")
        worksheet.write(fila, 10, "LEF")

        for registro in self.historico_eventos:
            fila += 1
            worksheet.write(fila, 0, registro[0].entidad.id)
            worksheet.write(fila, 1, registro[0].tiempo_ocurrencia)
            worksheet.write(fila, 2, registro[0].tipo)
            worksheet.write(fila, 3, registro[4])
            worksheet.write(fila, 4, registro[2])
            worksheet.write(fila, 5, registro[3])
            worksheet.write(fila, 6, registro[5])
            worksheet.write(fila, 7, registro[0].entidad.tiempo_llegada)
            worksheet.write(fila, 8, registro[0].entidad.tiempo_tarda)
            worksheet.write(fila, 9, registro[0].entidad.tiempo_salida)
            lista_eventos = "{"
            for evento in registro[1]:
                lista_eventos += "(" + str(evento.tiempo_ocurrencia) + \
                    "," + evento.tipo + ")"
            lista_eventos += "}"
            worksheet.write(fila, 10, lista_eventos)
            """
            """
        workbook.close()

"""
if __name__ == "__main__":
    nr = Simulacion(10, 8, 30, 7)
    nr.generarSimulacion()
    nr.generarEstadisticasExcel()
"""

