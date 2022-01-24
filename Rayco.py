import pandas

gastos = [0,0,0,0,0,0,0,0,0,0,0,0]
ingresos = [0,0,0,0,0,0,0,0,0,0,0,0]
indexColumn = 0
totalgastos = 0
totalingresos = 0

""""
Agregamos este comentario a modo de cambios en el proyecto

"""

try:
    data = pandas.read_csv('finanzas2020.csv', sep='\t')
except FileNotFoundError as e:
    print('El fichero no existe')
else:
    if (len(data.columns) == 12):
        for colum in data:
            for row in data.index:
                try:
                    valor = int(data[colum][row])
                    if( valor > 0):
                        ingresos[indexColumn] += int(data[colum][row])
                    else:
                        gastos[indexColumn] += int(data[colum][row])
                except ValueError as e:
                    print(f'No es entero {data[colum][row]}')
            totalgastos += gastos[indexColumn]    
            totalingresos += ingresos[indexColumn]    
            indexColumn = indexColumn + 1
        
        #print(ingresos)            
        #print(gastos)


        print('__________________________________________________________________________________________________________________________\n')
        print(f'El mes que mas gastos hubo fue : {data.columns[gastos.index(min(gastos))]} con un gasto de {min(gastos)}')
        print('__________________________________________________________________________________________________________________________\n')
        print(f'El mes que mas se ha ahorrado fue : {data.columns[gastos.index(max(gastos))]} con un gasto de {max(gastos)}')
        print('__________________________________________________________________________________________________________________________\n')
        print(f'La media de gastos al año es de : {totalgastos / 12}')
        print('__________________________________________________________________________________________________________________________\n')
        print(f'El gasto total a lo largo del año es de : {totalgastos}')
        print('__________________________________________________________________________________________________________________________\n')
        print(f'Los ingresos totales a lo largo del año es de : {totalingresos}')
        print('__________________________________________________________________________________________________________________________\n')
    else:
        print('El documento no contiene 12 columnas')
        

