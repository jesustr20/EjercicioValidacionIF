import functionsOperators

def operationSum():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        functionsOperators.suma(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        operationSum()

def operationSubstraction():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        functionsOperators.resta(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        operationSubstraction()

def operationMultiplication():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        functionsOperators.multi(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        operationMultiplication()

def operationDivision():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        functionsOperators.division(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        operationDivision()
    
def operationPotencia():
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el segundo numero: ")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        functionsOperators.potencia(num1,num2)
    else:
        print("Por favor, Ingresa numeros. Vuelve a intentarlo")
        operationPotencia()
