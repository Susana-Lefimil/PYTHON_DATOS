import datetime
import sqlalchemy
from sqlalchemy import text
import pandas as pd
#Una función que permita filtrar un DataFrame por fechas, indicando dataframe,
#columna para filtrar, fecha inicio y fecha fin. La función debe retornar un DataFrame.
def filtra_fecha_f(data,column, fecha_inicio,fecha_fin):
    '''Ingresar en orden; dataframe, columna de fecha a filtrar entre
      comillas simples, fecha inicio entre comillas (ymd) y fecha final entre comillas (ymd)'''
    data[column] = pd.to_datetime(data[column], format='%Y-%m-%d')
    df=data.loc[(data[column]>=fecha_inicio) & (data[column]<=fecha_fin)]
    return df


#Una función que permita generar reportes dependiendo de parámetros de entrada
#como dataframe, filas, columnas, valores y medida (funcion_agrupadora). Utilizar
#fill_value = 0. Esta función debe retornar un DataFrame pivotado.

def funcion_agrupadora_f(dataframe, indice, valores, medida):
    '''Ingresar dataframe, columna que se agrupara como indice de la tabla (indice),
       columna entre comillas simple o columnas en una lista (valores), finalmente la medida que se aplicará a las columnas
       (medida)'''
    
    df_pivot_f = pd.pivot_table(
                                   data = dataframe # DataFrame.
                                 , index = indice # Columna(s) del DataFrame original que queremos como indice de la tabla resultante.
                                 , values = valores # valores a lo que le aplicaremos la aggfunc.
                                 , aggfunc= medida # función a aplicar a la columna de valores.
                                 , fill_value=0
    )

    return df_pivot_f

#Una función que permita escribir en la base de datos a través del guardado de un
#DataFrame dependiendo de parámetros de entrada como DataFrame, nombre de la
#tabla, engine y comportamiento en caso de que exista la tabla (if_exists).


from sqlalchemy import text

def guardar_tabla_f(dataFrame, tabla, engine):
    ''' Ingresar data frame con el nombre de la columna de la tabla y sus valores respectivos que quiera ingresar,
        ingresar el nombre de la tabla entre comillas, ingrese la conexion con el motor de la base de datos'''
    dataFrame.to_sql(name=tabla, con=engine, if_exists='append',index=False)
    with engine.connect() as conn:
      conn.execute(text(f"SELECT * FROM {tabla}")).fetchall()

