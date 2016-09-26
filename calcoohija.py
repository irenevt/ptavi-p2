#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import calcoo

class CalculadoraHija(calcoo.Calculadora):

    def multiplicar(self, op1, op2):
        return op1 * op2


    def dividir(op1, op2):
        return op1 / op2


if __name__ == "__main__":

    calculadorahija = CalculadoraHija()

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    

    if sys.argv[2] == "suma":
        result = calculadorahija.sumar(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calculadorahija.restar(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = calculadorahija.multiplicar(operando1, operando2)
    elif sys.argv[2] == "divide":
        if sys.argv[3] == "0":
            sys.exit("No se puede dividir entre 0.")
        else:
            result = calculadorahija.div(operando1, operando2)
    else:
        sys.exit("Suma, resta, multiplica o divide.")

    print(result)
