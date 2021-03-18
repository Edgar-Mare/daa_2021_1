import time
import keyboard
t=0
bandera=True
decision=''
inicio = True
while inicio:
    decision=str(input('Iniciar s/n: '))
    if decision == "s":
        bandera = True
        while bandera:
            #time.sleep(1)
            print (t)
            t=t+1
            if keyboard.is_pressed('p'):
                print('se presionó parar!')
                print(f'Valor de contador: {t}')
                bandera=False

    elif decision == 'n':
        print('Bye bye!!')
        inicio = False
    else:
        time.sleep(1)
        print(f'Error "{decision}" no es una instrucción valida.')