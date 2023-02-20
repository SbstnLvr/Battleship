import numpy as np  
import random
tablero_jugador = np.full(fill_value = ' ', shape = (10, 10))
tablero_maquina = np.full(fill_value = ' ', shape = (10, 10))
tablero_jugador_a = np.full(fill_value = ' ', shape = (10, 10))
tablero_maquina_a = np.full(fill_value = ' ', shape = (10, 10))

def crear_tableros_barcos():
    
    lista_esloras = [4,3,3,2,2,2,1,1,1,1]   
    for eslora4 in lista_esloras:
        while True:
            # 'N' - 'S' - 'E' - 'O'
            orient = random.choice(['N', 'S', 'E', 'O'])

            # Posicion inicial del barco
            current_pos = np.random.randint(10, size = 2)
            
            fila = current_pos[0]
            col = current_pos[1]
            
            # Recogemos las 4 posiciones colindantes a current_pos
            coors_posiN = tablero_maquina[fila:fila - eslora4:-1, col]
            coors_posiE = tablero_maquina[fila, col: col + eslora4]
            coors_posiS = tablero_maquina[fila:fila + eslora4, col]
            coors_posiO = tablero_maquina[fila, col: col - eslora4:-1]
            
            # Comprobamos si esas posiciones son validas
            # Orientacion Norte
            if orient == 'N' and 0 <= fila - eslora4 < 10 and 'O' not in coors_posiN:
                tablero_maquina[fila:fila - eslora4:-1, col] = 'O'
                break

            # Orientacion Este
            elif orient == 'E' and 0 <= col + eslora4 < 10 and 'O' not in coors_posiE:
                tablero_maquina[fila, col: col + eslora4] = 'O'
                break

            # Orientacion Sur
            elif orient == 'S' and 0 <= fila + eslora4 < 10 and 'O' not in coors_posiS:
                tablero_maquina[fila:fila + eslora4, col] = 'O'
                break

            # Orientacion Oeste
            elif orient == 'O' and 0 <= col - eslora4 < 10 and 'O' not in coors_posiO:
                tablero_maquina[fila, col: col - eslora4:-1] = 'O'
                break

            # No cumple con las dimensiones del tablero, o hay un barco ahi
            # Probamos con otra coordenada
            else:
                continue
    
    lista_esloras = [4,3,3,2,2,2,1,1,1,1]
    for eslora4 in lista_esloras:
        while True:
            # 'N' - 'S' - 'E' - 'O'
            orient = random.choice(['N', 'S', 'E', 'O'])

            # Posicion inicial del barco
            current_pos = np.random.randint(10, size = 2)
            
            fila = current_pos[0]
            col = current_pos[1]
            
            # Recogemos las 4 posiciones colindantes a current_pos
            coors_posiN = tablero_jugador[fila:fila - eslora4:-1, col]
            coors_posiE = tablero_jugador[fila, col: col + eslora4]
            coors_posiS = tablero_jugador[fila:fila + eslora4, col]
            coors_posiO = tablero_jugador[fila, col: col - eslora4:-1]
            
            # Comprobamos si esas posiciones son validas
            # Orientacion Norte
            if orient == 'N' and 0 <= fila - eslora4 < 10 and 'O' not in coors_posiN:
                tablero_jugador[fila:fila - eslora4:-1, col] = 'O'
                break

            # Orientacion Este
            elif orient == 'E' and 0 <= col + eslora4 < 10 and 'O' not in coors_posiE:
                tablero_jugador[fila, col: col + eslora4] = 'O'
                break

            # Orientacion Sur
            elif orient == 'S' and 0 <= fila + eslora4 < 10 and 'O' not in coors_posiS:
                tablero_jugador[fila:fila + eslora4, col] = 'O'
                break

            # Orientacion Oeste
            elif orient == 'O' and 0 <= col - eslora4 < 10 and 'O' not in coors_posiO:
                tablero_jugador[fila, col: col - eslora4:-1] = 'O'
                break

            # No cumple con las dimensiones del tablero, o hay un barco ahi
            # Probamos con otra coordenada
            else:
                continue
            
crear_tableros_barcos()

def imprimir_tablero_barco():
    print("")
    print("tablero_jugador:")
    print("")
    print(tablero_jugador)
    print("")

def actualizar_tablero_jugador():
    print("")
    print("tablero_jugador:")
    print("")
    print(tablero_jugador_a)
    print("") 
    print(Contador_esloras_jugador())
    print("")

def actualizar_tablero_maquina():
    print("")
    print("tablero_maquina:")
    print("")
    print(tablero_maquina_a)
    print("")
    print(Contador_esloras_maquina()) 
    print("")

def Contador_esloras_maquina():
        maska = np.array([])
        maska = tablero_maquina_a == "X"
        tablero_maquina_a[maska]
        vidas_maquina = (20-len(tablero_maquina_a[maska]))
        print("Esloras restantes de la maquina: ", vidas_maquina)
        return vidas_maquina

def Contador_esloras_jugador():
        maskb = np.array([])
        maskb = tablero_jugador_a == "X"
        tablero_jugador_a[maskb]
        vidas_jugador = (20-len(tablero_jugador_a[maskb]))
        print("Esloras restantes del jugador: ", vidas_jugador)
        return vidas_jugador

def Disparos_a_la_maquina():

    while True:

        try:
                    
                    DisparoColumna = int(input("Introduce las coordenadas de la columna, del 1 al 10 por favor: "))-1
                    DisparoFila = int(input("Introduce las coordenadas de la fila, del 1 al 10 por favor: "))-1
                    DisparoJugador = [(DisparoFila, DisparoColumna)]
                
                    if not 0 <= DisparoColumna <= 9 or not 0 <= DisparoFila <= 9:
			                #if columna < 0 or columna > 9 or fila < 0 or fila > 9:
                        raise ValueError('Valore fuera de rango')
                    
                    break
        
        except ValueError:
                    
                    print("Sólo se admiten valores entre el 1 y 10.")
			

    if tablero_maquina[(DisparoFila, DisparoColumna)] == " ":
        for i in DisparoJugador:
            tablero_maquina_a[i] = "M"  
        actualizar_tablero_maquina() 
        Disparos_al_jugador()
    elif tablero_maquina_a[(DisparoFila, DisparoColumna)] == "M":
        Disparos_a_la_maquina()
    elif tablero_maquina[(DisparoFila, DisparoColumna)] == "O":
        for i in DisparoJugador:
            tablero_maquina_a[i] = "X" 
        actualizar_tablero_maquina()   
        if Contador_esloras_maquina() > 16:
            Disparos_a_la_maquina()
        else:
            print("Has Ganado")
            
    elif tablero_maquina_a[(DisparoFila, DisparoColumna)] == "X":
        Disparos_a_la_maquina()
    else:   
        print("no se ni como has llegado aqui tio")
    return tablero_maquina_a

def Disparos_al_jugador():
    DisparoFila= np.random.randint(0,10)
    DisparoColumna= np.random.randint(0,10)
    DisparoMaquina = [(DisparoFila, DisparoColumna)]
    
    if tablero_jugador[(DisparoFila, DisparoColumna)] == " ":
        for i in DisparoMaquina:
            tablero_jugador_a[i] = "M" 
        actualizar_tablero_jugador()   
        imprimir_tablero_barco()
        Disparos_a_la_maquina()    
    elif tablero_jugador_a[(DisparoFila, DisparoColumna)] == "M":
        Disparos_al_jugador()
    elif tablero_jugador[(DisparoFila, DisparoColumna)] == "O":
        for i in DisparoMaquina:
            tablero_jugador_a[i] = "X" 
        actualizar_tablero_jugador() 
        if Contador_esloras_jugador() > 16:
            Disparos_al_jugador()
        else:
            print("Has Perdido")
                  
    elif tablero_jugador_a[(DisparoFila, DisparoColumna)] == "X":
        Disparos_al_jugador()
    else:   
        print("no se ni como has llegado aqui tio")
    return tablero_jugador_a


def Jugar():
    imprimir_tablero_barco()
    Disparos_a_la_maquina()
    