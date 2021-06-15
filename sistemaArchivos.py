posicion=0
texto=''
numero_elementos=0
principal=""
tipo_archivo=".txt"

def leertxt():
    global principal
    archivo_txt=open("Sistema_gestor.sa","r")
    texto=archivo_txt.read()
    #archivo_txt.close()
    texto=texto.split("\n")
    lineas=len(texto)/4
    archivo_txt.close()
    return texto

def nuevo_archivo(texto):
    archivo_txt=open("Sistema_gestor.sa","a")
    archivo_txt.write(texto)
    archivo_txt.close()

def examinar():
    archivos=leertxt()
    for i in range (len(archivos)):
        if tipo_archivo in archivos[i]:
            print(archivos[i])
        else:
            
            print(f'{archivos[i]} es una carpeta')


def crear_carpeta(nombre):
    archivo_txt=open("Sistema_gestor.sa","a")
    archivo_txt.write(texto)
    archivo_txt.close()


#def guardar_archivo


#nuevo_archivo("huevos.txt")
#print(leertxt())
examinar()