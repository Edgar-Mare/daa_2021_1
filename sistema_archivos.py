class arbol:
    raiz = None
    hijos = []

    def __init__(self, nombre,hijos):
        self.raiz = nombre
        self.hijos = hijos

def leerArchivo(nombre,baseSA):
    indice = 0
    linea = baseSA[indice]
    while (not linea.find(nombre)>=0):
        indice +=1
        linea=baseSA[indice]
    linea+=1
    
    while (not linea.find("#")>=0):
        print (linea)
        indice += 1
        linea = baseSA[indice]

datosSA = open("sistemadearchivos.sa","r")
bas