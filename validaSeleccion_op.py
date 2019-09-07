import logica_op
import validaDato_op
import os


def validar_opc(elegir):
    if elegir == '1' or elegir == "Suma" or elegir == "+":
        os.system("cls") #limpia la pantalla
        print("Realizar su Suma: ")
        print()
        validaDato_op.valida_datoSum()

    elif elegir == '2' or elegir == "Resta" or elegir == "-":
        os.system("cls")
        print("Realizar su Resta: ")
        print()
        validaDato_op.valida_datoResta()

    elif elegir == '3' or elegir == "Multiplicacion" or elegir == "*":
        os.system("cls")
        print("Realizar su Multiplicacion: ")
        print()
        validaDato_op.valida_datoMul()

    elif elegir == '4' or elegir == "Division" or elegir == "/":
        os.system("cls")
        print("Realizar su Division: ")
        print()
        validaDato_op.valida_datoDivi()

    elif elegir == '5' or elegir == "Potencia" or elegir == "**":
        os.system("cls")
        print("Realizar su Potencia: ")
        print()
        validaDato_op.valida_datoPoten()
    
    elif elegir == '6' or elegir == "Salir":
        print("Saliste de la calculadora...")
        exit()
    else:
        print("Ingresa la opcion correcta.")
       