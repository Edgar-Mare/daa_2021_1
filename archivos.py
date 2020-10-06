class stack:
  def __init__ (self):
    self.__datos=[]

  def is_empty(self):
    return len(self.__datos)==0

  def get_top(self):
    return self.__datos[-1]

  def pop(self):
    return self.__datos.pop()

  def push(self,valor):
    self.__datos.append(valor)

  def get_length(self):
    return len(self.__datos)

  def to_string(self):
    print('--------------------')
    for ele in self.__datos[-1::-1]:
      print(f'{ele}')
    print('--------------------')




import re
contador=0
pila=stack()


patron_parentesi=re.compile(r'\(')
patron_parentesisCierre=re.compile(r'\)')
patron_corchete=re.compile(r'\[')
patron_corcheteCierre=re.compile(r'\]')
patron_llave=re.compile(r'\{')
patron_llaveCierre=re.compile(r'\}')

f = open("prueba.java", "r")
while(True):
    linea = f.readline()

    resultado_parentesis=re.search(patron_parentesi,linea)
    resultado_parentesisCierre=re.search(patron_parentesisCierre,linea)
    resultado_corchete=re.search(patron_corchete,linea)
    resultado_corcheteCierre=re.search(patron_corcheteCierre,linea)
    resultado_llave=re.search(patron_llave,linea)
    resultado_llaveCierre=re.search(patron_llaveCierre,linea)


    if resultado_parentesis != None:
      pila.push('parentesis no cerrado')

    if resultado_parentesisCierre !=None:
        if pila.is_empty():
            pila.push('Falta parentesis de apertura')
        else:
            pila.pop()


    if resultado_corchete != None:
      pila.push('corchete no cerrado')

    if resultado_corcheteCierre !=None:
        if pila.is_empty():
            pila.push('Falta parentesis de apertura')
        else:
            pila.pop()


    if resultado_llave != None:
      pila.push('pico parentesis no cerrado')

    if resultado_llaveCierre !=None:
        if pila.is_empty():
            pila.push('Falta parentesis de apertura')
        else:
            pila.pop()

    if not linea:

        break
f.close()

print(f'{pila.to_string()}')
if pila.is_empty():
    print('Esta balanceado')
else:
    print('No esta balanceado')