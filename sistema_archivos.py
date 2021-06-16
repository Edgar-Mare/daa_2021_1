from tkinter import *
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb


def abrir_ventana():
    leer=easygui.fileopenbox()
    return leer

#----------------------------
def abrir_archivo():
    ruta = abrir_ventana()
    try:
        os.startfile(ruta)
    except:
        mb.showinfo('Advertencia', "Archivo no encontrado!")

#-----------------------------
def borrar_archivo():
    borrador = abrir_ventana()
    if os.path.exists(borrador):
        os.remove(borrador)             
        mb.showinfo('Advertencia', "Archivo borrado con éxito!")

    else:
        mb.showinfo('Advertencia', "Archivo no encontrado!")

#-----------------------------
def renombrar_archivo():
    ventana = abrir_ventana()
    ruta1 = os.path.dirname(ventana)
    extension=os.path.splitext(ventana)[1]
    print("Dame el nuevo nombre del archivo")
    nuevo_name=input()
    ruta = os.path.join(ruta1, nuevo_name+extension)
    print(ruta)
    os.rename(ventana,ruta) 
    mb.showinfo('Advertencia', "Archivo renombrado !")

#-------------------------------
def copiar_archivo():
    ruta1 = abrir_ventana()
    destino=filedialog.askdirectory()
    shutil.copy(ruta1,destino)
    mb.showinfo('Advertencia', "Archivo copiado con éxito !")

#-------------------------------
def mover_archivo():
    rutaI = abrir_ventana()
    rutaD =filedialog.askdirectory()
    if(rutaI==rutaD):
        mb.showinfo('Advertenia', "No moviste el archivo")
    else:
        shutil.move(rutaI, rutaD)  
        mb.showinfo('Advertencia', "Archivo movido con éxito !")

#------------------------------
def crear_carpeta():
    rutaCarpeta = filedialog.askdirectory()
    print("Dame el nombre de la carpeta")

    carpetaNombre=input()
    ruta = os.path.join(rutaCarpeta, carpetaNombre)  

    os.mkdir(ruta)
    mb.showinfo('Advertencia', "Carpeta creada con éxito !")

#-------------------------------
def borrar_carpeta():
    borrador = filedialog.askdirectory()
    os.rmdir(borrador)
    mb.showinfo('Advertencia', "Carpeta borrada con éxito !")

#--------------------------------
def lista_archivos():
    lista_carpetas = filedialog.askdirectory()
    lista_ordenada=sorted(os.listdir(lista_carpetas))       
    i=0
    print("Archivos en ", lista_carpetas, "carpeta hay:")
    while(i<len(lista_ordenada)):
        print(lista_ordenada[i]+'\n')
        i+=1

#-------------------------------

def obtener_ruta():
    ruta=os.getcwd()
    mb.showinfo('Advertencia', ruta)

#---------------------------------
def crear_archivo():
    ruta_archivo=filedialog.askdirectory()
    print("Dame el nombre del archivo")
    nombre_archivo=input()
    ruta = os.path.join(ruta_archivo, nombre_archivo) 
    #print(ruta)
    archivo=open(ruta,'w')
    archivo.write("primera linea"+os.linesep)
    archivo.write("Segunda linea")
    archivo.close()
    mb.showinfo('Advertencia', "Archivo creado con éxito !")
root = Tk()
#canv = Canvas(root, width=500, height=0, bg='white')
#canv.grid(row=0, column=2)

#img = PhotoImage(file='/home/edgar/Downloads/Archivero.png')  
#canv.create_image(20, 20, anchor=NW, image=img)

Label(root, text="Sistema de archivos GOKOMA", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)

Button(root, text = "Abrir archivo", command = abrir_archivo).grid(row=15, column =2)

Button(root, text = "Copiar archivo", command = copiar_archivo).grid(row = 25, column = 2)

Button(root, text = "Borrar archivo", command = borrar_archivo).grid(row = 35, column = 2)

Button(root, text = "Renombrar archivo", command = renombrar_archivo).grid(row = 45, column = 2)

Button(root, text = "Mover archivo", command = mover_archivo).grid(row = 55, column =2)

Button(root, text = "Crear carpeta", command = crear_carpeta).grid(row = 75, column = 2)

Button(root, text = "Eliminar carpeta", command = borrar_carpeta).grid(row = 65, column =2)

Button(root, text = "Ver archivos", command = lista_archivos).grid(row = 85,column = 2)

Button(root, text = "Ver ruta", command = obtener_ruta).grid(row = 95,column = 2)

Button(root, text = "Crear archivo", command = crear_archivo).grid(row = 105,column = 2)

root.mainloop()