### Función para convertir un número entero en su equivalente en números romanos. ###
def int_to_roman(n):
    ### Tabla de equivalencias de números romanos. ###
    roman_numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman = '' ### String vacío para almacenar el número romano. ###
    ### Para cada equivalencia romana de la lista anterior le agregamos al string vacío la equivalencia más grande que tiene la fecha dada y luego se le quita el valor del numeral para seguir agregando los valores restantes con sus numerales romanos correspondientes. ###
    for value, r_numeral in roman_numerals: 
        while n >= value:
            roman += r_numeral
            n -= value
    return roman

### Leer la entrada de las fechas. ###
input_str = input()
parts = input_str.split('-')
### Sección para verificar el formato de las fechas. ###
if len(parts) != 2:
    print("Error: Formato de fecha inválido")
else:
    a_str, b_str = parts
    if not a_str[:-2].isdigit() or not b_str[:-2].isdigit():
        print("Error: Formato de fecha inválido")
    elif a_str[-2:] not in ['AD','BC']:
        print("Error: Formato de fecha inválido")
    elif b_str[-2:] not in ['AD','BC']:
        print("Error: Formato de fecha inválido")


    else:
    ### Convertir los años a números enteros. ###
    ### Al ser un calendario romano, este inicia en el año 753, por lo que al calendario gregoriano, cuando es 'BC', se tiene que restar 753 años para llegar a su año 0. Al ser 'AD' se suma 753 porque en el gregoriano se reinicia a 0 al pasar de BC a AC, por lo que hay que tomar en cuenta ese "reinicio" ###
        if a_str.endswith('BC'):
            a_num = 754 - int(a_str[:-2])
        elif a_str.endswith('AD'):
            a_num = int(a_str[:-2]) + 753
        if b_str.endswith('BC'):
            b_num = 754 - int(b_str[:-2])
        elif b_str.endswith('AD'):
            b_num = int(b_str[:-2]) + 753
        else:
            print("Error: Formato de fecha inválido")

            
        ### Encontrar el rango completo de años y convertir cada año a números romanos. ###
        if a_num > b_num:
            print('Error: Rango de fechas inválida')
        elif 0 <= a_num <= a_num <= 2766:
            year_range = range(a_num, b_num)
            roman_years = [int_to_roman(year) for year in year_range]

            ### Encontrar el número máximo de símbolos necesarios para cualquier año en el rango. ###
            max_symbols = len(max(roman_years, key=len))
            ### Imprimir el resultado. ###
            print(max_symbols)
        else:
            print('Error: Rango de fechas inválida')
