from Conjunto import Conjunto

def opcion0(c1,c2):
    print("Adiós")

def unirConjuntos(c1,c2):
    c3 = c1 + c2
    c3.Mostrar()

def difConjuntos(c1,c2):
    c3= c1 - c2
    c3.Mostrar()

def igualConjuntos(c1,c2):
    print (c1 == c2)

switcher = {
    0: opcion0,
    1: unirConjuntos,
    2: difConjuntos,
    3: igualConjuntos
}

def switch(argument,conjunto1,conjunto2):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(conjunto1,conjunto2)

if __name__ == '__main__':

    unConjunto = Conjunto()
    lim = input('Ingrese la cantidad de enteros que quiere agregar al primer conjunto: ')
    if (lim.isdigit()):
        for i in range(int(lim)):
            entero = input('Ingrese el entero N° ' + str(i+1) + ' a agregar al conjunto: ')
            if (entero.isdigit()):
                unConjunto.agregarElem(int(entero))
            else:
                print('Valor inválido (no es un entero)')
    else:
        print('La cantidad de enteros debe ser un entero.')
    unConjunto.Mostrar()

    otroConjunto = Conjunto()
    lim = input('Ingrese la cantidad de enteros que quiere agregar al primer conjunto: ')
    if (lim.isdigit()):
        for i in range(int(lim)):
            entero = input('Ingrese el entero N° ' + str(i+1) + ' a agregar al conjunto: ')
            if (entero.isdigit()):
                otroConjunto.agregarElem(int(entero))
            else:
                print('Valor inválido (no es un entero)')
    else:
        print('La cantidad de enteros debe ser un entero.')
    otroConjunto.Mostrar()

    bandera = False
    while not bandera:
        print("")
        print("0 Salir")
        print("1 Unir conjuntos")
        print("2 Diferencia de conjuntos ")
        print("3 Verificar si los conjuntos son iguales")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion,unConjunto,otroConjunto)
        bandera = int(opcion)==0
