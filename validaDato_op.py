import logica_op

def valida_datoSum():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        logica_op.suma(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        valida_datoSum()

def valida_datoResta():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        logica_op.resta(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        valida_datoResta()

def valida_datoMul():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        logica_op.multi(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        valida_datoMul()

def valida_datoDivi():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        logica_op.division(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        valida_datoDivi()
    
def valida_datoPoten():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        logica_op.potencia(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        valida_datoPoten()
