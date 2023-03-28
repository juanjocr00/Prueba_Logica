def direction(n, m):
## Si n > m, entonces la dirección final sólo podría ser Arriba o Abajo dependiendo del valor de m porque siempre quedará alguna celda en la última y llegas a la ultima columna desde alguna fila abajo o arriba. ###
    if n > m:
        ### Si 'm' es par, significa no hay solo una columna en medio, lo que obliga que se de un giro extra hacia arriba viniendo de la columna de la derecha (⮤). ###
        if m % 2 == 0:
            print("U") # Up (Arriba)
        ### Al 'm' ser impar, significa hay una única columna en medio, lo que significa que habrá un giro hacia abajo viniendo de la columna de la izquierda (↴). ###
        else:
            print("D") # Down (Abajo)
### Si m > n, aplica lo mismo que lo anterior, pero al ser un tabla acostada, en vez de que la ultima columna vengas de un alguna fila antes, vienes de una columna diferente, solo moviéndose la columna de izquierda o derecha. ###
### Else también toma en cuenta m=n. ###
    else:
        ### si 'n' es par, significa no hay solo una fila en medio, lo que obliga que se de un giro extra hacia la izquierda viniendo de la fila de arriba(↲). ###
        if n % 2 == 0:
            print("L") # Left (Izquierda)
        ### Al 'n' ser impar, significa hay una única columna en medio, lo que significa que habrá un giro hacia la derecha viniendo de la columna de la abajo (↱). ###
        else:
            print("R") # Right (Derecha) 
            
### Obtener los inputs. ###
T = int(input()) ### T = Número de pruebas. ###
if 1 <= T <= 5000:
    for i in range(T):
        n, m = map(int, input().split()) ### 'n' son las filas y 'm' son las columnas de la tabla. ###
        if 1 <= n <= 10**9 and 1 <= m <= 10**9:
            direction(n, m) ### Llama la función para encontrar la dirección. ###
        else:
            print("Error: no es válida la tabla") ### La fila o columna dada no se encuentra en el rango válido establecido. ###
            break
else:
    print("Error: número de pruebas inválido") ### El número de pruebas no se encuentra en el rango válido establecido. ###
