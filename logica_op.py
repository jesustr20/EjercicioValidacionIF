import validaDato_op

def suma(a,b):
    sumt = 0
    sumt = a + b
    print(f"La respuesta es: {sumt}")

def resta(a,b):
    res = 0
    res = a-b
    print(f"La respuesta es: {res}")

def multi(a,b):
    mul = 0
    mul = a*b
    print(f"La respuesta es: {mul}")

def division(a,b):
    div = 0
    if b == 0:
        print(f"Error, no puede ser dividido '{a}/{b}', intenta de nuevo ")
        validaDato_op.valida_datoDivi()
    else:
        div = a/b
        print(f"La respuesta es: {div}")

def potencia(a,b):
    pote = 0
    pote = a**b
    print(f"La respuesta es: {pote}")