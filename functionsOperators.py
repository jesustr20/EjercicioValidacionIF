import operations

def suma(a,b):
    sumt = a + b
    print(f"La respuesta es: {sumt}")

def resta(a,b):
    res = a-b
    print(f"La respuesta es: {res}")

def multi(a,b):
    mul = a*b
    print(f"La respuesta es: {mul}")

def division(a,b):
    div = 0
    if b == 0:
        print(f"Error, no puede ser dividido '{a}/{b}', intenta de nuevo ")
        operations.valida_datoDivi()
    else:
        div = a/b
        print(f"La respuesta es: {div}")

def potencia(a,b):
    pote = a**b
    print(f"La respuesta es: {pote}")