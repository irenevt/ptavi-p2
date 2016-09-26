#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import sys
import calcoohija

fichero = sys.argv[1]
with open(fichero) as ficheroOperaciones:

    datos = csv.reader(ficheroOperaciones)
    calcplus = calcoohija.CalculadoraHija()

    for linea in datos:
        numeros = linea[1:]
        operacion = linea[0]
        result = int(numeros[0])

        if operacion == "suma":
            for i in range(1, len(numeros)):
                result = calcplus.sumar(result, int(numeros[i]))
        elif operacion == "resta":
            for i in range(1, len(numeros)):
                result = calcplus.restar(result, int(numeros[i]))
        elif operacion == "multiplica":
            for i in range(1, len(numeros)):
                result = calcplus.multiplicar(result, int(numeros[i]))
        elif operacion == "divide":
            for i in range(1, len(numeros)):
                if int(numeros[i]) == "0":
                    sys.exit("No se puede dividir entre cero")
                else:
                    result = calcplus.dividir(result, int(numeros[i]))
        else:
            sys.exit("Escribe de nuevo: Suma, resta, multiplica o divide")

        print(result)
