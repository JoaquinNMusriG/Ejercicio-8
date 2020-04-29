import numpy as np

class Conjunto:
    __numEnteros = np.empty(0, dtype = int)

    def __init__ (self):
        self.__numEnteros = np.empty(0, dtype = int)

    def Mostrar (self):
        print('El conjunto es: ')
        for elem in self.__numEnteros:
            print('%d '% (elem), end = '')
        print()

    def agregarElem (self, elem):
        self.__numEnteros = np.append(self.__numEnteros,elem)

    def getLong (self):
        return self.__numEnteros.size

    def getElem(self, i):
        return self.__numEnteros[i]

    def verifPertenencia(self, elem):
        if elem in self.__numEnteros:
            return False
        return True

    def verifDesigualdad(self, elem, i):
        if self.__numEnteros[i] != elem:
            return True
        return False

    def __add__ (self, otroC):
        resultado = Conjunto()
        i = 0
        j = 0
        band = True
        for i in range(otroC.getLong()):
            if (resultado.verifPertenencia(otroC.getElem(i))):
                resultado.agregarElem(otroC.getElem(i))
        i = 0
        j = 0
        while i in range(self.getLong()):
            while (j in range(resultado.getLong())) & band:
                if(resultado.verifDesigualdad(self.__numEnteros[i],j)):
                    if (resultado.verifPertenencia(self.__numEnteros[i])):
                        resultado.agregarElem(self.__numEnteros[i])
                        band = False
                else:
                    band = False
                j += 1
            band=True
            j = 0
            i += 1

        return resultado

    def eliminarElem(self, i):
        self.__numEnteros = np.delete(self.__numEnteros,i)

    def __sub__ (self, otroC):
        resultado = Conjunto()
        i = 0
        j = 0
        band = True
        for i in range(self.getLong()):
            if (resultado.verifPertenencia(self.getElem(i))):
                resultado.agregarElem(self.getElem(i))
        i = 0
        j = 0
        while i in range(otroC.getLong()):
            while (j in range(resultado.getLong())) & band:
                if not(resultado.verifDesigualdad(otroC.getElem(i),j)):
                    resultado.eliminarElem(j)
                    band = False
                j += 1
            band=True
            j = 0
            i += 1

        return resultado

    def __eq__ (self, otroC):
        if (self.getLong() != otroC.getLong()):
            return False
        else:
            i = 0
            j = 0
            band = True
            while i in range(self.getLong()):
                while (j in range(otroC.getLong())) & band:
                    if(self.verifDesigualdad(otroC.getElem(j),i)):
                        if (otroC.verifPertenencia(self.__numEnteros[i])):
                            return False
                        band = False
                    else:
                        band = False
                    j += 1
                band=True
                j = 0
                i += 1
        return True
