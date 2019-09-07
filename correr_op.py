import validaSeleccion_op


elegir = input("Elige una opcion:\n1: Suma o '+'."+
                                "\n2: Resta o '-'."+
                                "\n3: Multiplicacion o '*'."+
                                "\n4: Division o '/'."+
                                "\n5: Potencia o '**'."+
                                "\n6: Salir."+
                                "\nSelecciona: ")
validaSeleccion_op.validar_opc(elegir)