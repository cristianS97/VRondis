import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

path_name = 'C:\\Users\\user\\Desktop\\test brondis\\Pregunta 2'
file_name = 'sicas11022020103820_test_exam.csv'

def crear_conexion():
    conection = sqlite3.connect(f"{path_name}\\bd_prueba.db")
    return conection

data = pd.read_csv(f'{path_name}\\{file_name}', encoding='iso-8859-1')

data.head()

print(data.shape)

# Creamos y rellenamos la tabla de la base de datos con la información del dataframe

try:
    conection = crear_conexion()
    data.to_sql(con=conection, name='facturas')
    conection.close()
except ValueError:
    print('La tabla facturas ya existe')

conection = crear_conexion()
cursor = conection.cursor()
cursor.execute('select * from facturas')
info = cursor.fetchall()
conection.close()

print(len(info))

data_patente1 = data[data['PATENTE'] == 'DDBD38']
print(f'Se han encontrado {len(data_patente1)} transacciones correspondientes a la patente DDBD38')

data_patente2 = data[data['PATENTE'] == 'KSVX99']
print(f'Se han encontrado {len(data_patente2)} transacciones correspondientes a la patente KSVX99')

data_rendido = data[data['ESTADO'] == 'Rendido']
print(f'La cantidad de transacciones con estado rendido son {len(data_rendido)} transacciones')

data_fecha = data[data['F.INGRESO'] >= '01/01/2020']
print(f'La cantidad de transacciones con fecha posterior a 01/01/2020 son {len(data_fecha)} transacciones')

data['F.INGRESO'] = pd.to_datetime(data['F.INGRESO'])

data_fecha = data[data['F.INGRESO'] >= '2020-01-01']
print(f'La cantidad de transacciones con fecha posterior a 01/01/2020 son {len(data_fecha)} transacciones')

data_final = pd.concat([data_rendido, data_fecha], axis=0)
print(data_final.shape)

print(data_final)

data_final.to_csv(path_name + '\\export_data.csv', index=False)