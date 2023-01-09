import helpers
import operations
import platform

TYPE_PLATFORM = platform.system()

def validateSelection(select):
    match select:
        case '1':            
            helpers.whatSystem(TYPE_PLATFORM)            
            print("Sum Operation: ")
            operations.operationSum()
        case '2':
            helpers.whatSystem(TYPE_PLATFORM)
            print("Substraction Operation: ")
            operations.operationSubstraction()
        case '3':
            helpers.whatSystem(TYPE_PLATFORM)
            print("Multiplication Operation: ")
            operations.operationMultiplication()
        case '4':
            helpers.whatSystem(TYPE_PLATFORM)
            print("Division Operation: ")
            operations.operationDivision()
        case '5':
            helpers.whatSystem(TYPE_PLATFORM)
            print("Potencia Operation: ")
            operations.operationPotencia()
        case '6':
            helpers.whatSystem(TYPE_PLATFORM)
            print("Saliste de la calculadora...")
            exit()
        case _: # Default
            helpers.whatSystem(TYPE_PLATFORM)
            print("Ingresa la opcion correcta.")
  