import numpy as np


#tablero
tablero = [[" " for _ in range(10)] for _ in range(10)]
for fila in tablero: print(fila)


print("Bienvenido a hundir la flota!!")

# Insertar barco horizontal de 4 casillas
for j in range(4):
    tablero[7][j] = "B"

# Insertar barco vertical de 3 casillas
for i in range(3, 6):
    tablero[i][6] = "B"
for i in range(3, 6):
    tablero[i][2] = "B"
    
# Insertar barco horizontal de 2 casillas
for j in range(2):
    tablero[1][j] = "B"
for j in range(2):
    tablero[2][j] = "B"
    
for fila in tablero: print(fila)


#disparo
try:
    i = input ("Di tu primera coordenada, del 0 al 9: ")
    j = input ("Di la segunda coordenada, del 0 al 9: ")
    i = int(i)
    j = int(j)
except ValueError:
    print("Por favor, introduce solo numeros!")
    

# Comprobar el estado de la casilla
if tablero[i][j] == "B":
    tablero[i][j] = "x"
    print(f"Tocado en posición {i},{j}")
elif tablero[i][j] == " ":
    tablero[i][j] = "o"
    print("Agua")
else:
    print("Ya habías disparado en esta posición.")
    
# print(tablero)
for fila in tablero: print(fila)