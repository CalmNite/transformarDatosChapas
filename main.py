import pandas as pd
import numpy as np
import os


df = pd.read_csv(os.getenv("URL"))
lista = [] 
      
poligonos = df['POLIGONO'].unique()

# For each unique 'POLIGONO' value
for poligono in poligonos:
    # Filter the DataFrame
    df_filtered = df[df['POLIGONO'] == poligono]
   
    # Ensure 'Latitud' and 'Longitud' are floats 
    df_filtered['LATITUD'] = df_filtered['LATITUD'].astype(float)
    df_filtered['LONGITUD'] = df_filtered['LONGITUD'].astype(float)

    columns_to_add = ['Chapa Instalada', 'Tipo Carretera', 'Acceso Libre Vehículos', 'Foto Entorno', 'Motivos No Instalación', 'Otro Motivo', 'Completado']
    for column in columns_to_add:
        df_filtered[column] = np.nan 
    # Create the 'Maps' column as a composition
    df_filtered['MAPS'] = 'https://maps.google.com/maps?q=' + df_filtered['LATITUD'].astype(str) + ',' + df_filtered['LONGITUD'].astype(str)
    
    # Only keep the columns you want
    columns_to_keep_excel = ['CODIGOEMERGENCIA', 'Chapa Instalada', 'Tipo Carretera', 'Acceso Libre Vehículos', 'Foto Entorno', 'Motivos No Instalación', 'Otro Motivo', 'Completado', 'LATITUD', 'LONGITUD', 'MAPS']
    columns_to_keep_csv = ['CODIGOEMERGENCIA', 'LATITUD', 'LONGITUD']

    df_filtered_excel = df_filtered[columns_to_keep_excel]
    df_filtered_csv = df_filtered[columns_to_keep_csv]
    
    # Save the filtered DataFrame to a CSV file
    df_filtered_excel.to_excel(f'{os.getenv("FILE_NAMES")}{poligono}.xlsx', index=False, engine='openpyxl')
    df_filtered_csv.to_csv(f'{os.getenv("FILE_NAMES")}{poligono}.csv', index=False)


