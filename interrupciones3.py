import time
import keyboard
count=0
bandera_keyboard=True
bandera_contador=True
decision=''
inicio = True



while inicio:
    decision=str(input('Iniciar s/n: '))
    if decision == "s":
        bandera_keyboard = True
        bandera_contador = True

        while bandera_keyboard and bandera_contador:
            
            time.sleep(0.001)
          
            print (count)
            count=count+1
            if count % 1000 == 0:
                print(f'Se realizaron {count} iteraciones')
                bandera_contador = False

            if keyboard.is_pressed('p'):
                print('se presionó parar!')
                print(f'Valor de contador: {count}')
                bandera_keyboard=False

    elif decision == 'n':
        print('Bye bye!!')
        inicio = False
    else:
        time.sleep(1)
        print(f'Error "{decision}" no es una instrucción valida.')
