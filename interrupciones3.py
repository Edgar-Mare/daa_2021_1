import time
import keyboard
count=0
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

            if keyboard.is_pressed('p'):#Interrupción por teclado (interrupción por hardware)
                print('se presionó parar!')
                print(f'Valor de contador: {count}')
                bandera_keyboard=False

    elif decision == 'n':
        print('Bye bye!!')
        inicio = False
    else:
        time.sleep(1)
        print(f'Error "{decision}" no es una instrucción valida.')
