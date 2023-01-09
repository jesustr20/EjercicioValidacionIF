import selector


select = input("Elige una opcion:\n1: Suma"+
                                "\n2: Resta"+
                                "\n3: Multiplicacion"+
                                "\n4: Division"+
                                "\n5: Potencia"+
                                "\n6: Salir."+
                                "\nSelecciona: ")
selector.validateSelection(select)