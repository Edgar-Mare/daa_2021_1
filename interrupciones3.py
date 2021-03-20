import time
import keyboard

inicioTiempo=time.time()

count=0
tiempo_contador= False
bandera_keyboard=True
bandera_contador=True
decision=''
inicio = True



while inicio: #Punto base del sitema
    decision=str(input('Iniciar s/n: '))
    if decision == "s":
        bandera_keyboard = True
        bandera_contador = True

        while bandera_keyboard and bandera_contador:#Requisitos para activar las interrupciones
            
            time.sleep(0.001)
          
            print (count)
            count=count+1
            
            

            if count % 1000 == 0: #Interrupción por numero de iteraciones  (interrupción por software)
                print(f'Se realizaron {count} iteraciones')
                bandera_contador = False
                tiempo_contador = True

            if keyboard.is_pressed('p'):#Interrupción por teclado (interrupción por hardware)
                print('se presionó parar!')
                print(f'Valor de contador: {count}')
                bandera_keyboard=False
                tiempo_contador = True

        while tiempo_contador: # Interrupcion si se genera una interrupcion y no se trata en menos de un lapso de 5 segundos
            if (time.time() - inicioTiempo) % 5 == 0:
                print('Interrupcion tiempo')
                decision=str(input('¿continuar s/n ?: '))
                if decision == "s":
                    tiempo_contador = False
                    bandera_keyboard = True
                    bandera_contador = True

                elif decision == 'n':
                    tiempo_contador = False
                    inicio = False
                else:
                    print('Error')

    elif decision == 'n':
        print('Bye bye!!')
        finTiempo = (time.time() - inicioTiempo)
        print(finTiempo)
        inicio = False
    else:
        time.sleep(1)   
        print(f'Error "{decision}" no es una instrucción valida.')
