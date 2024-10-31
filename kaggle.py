# Importa la librería Pandas, fundamental para analisis de datos
import pandas as pd
# Define la ruta del archivo CSV que contiene los datos
# Si el archivo está en el mismo directorio, basta ocn poner el nombre del archivo
path = 'G:\Estudio\IA\Kaggle\dragon_ball_z.csv'
dragon_data = pd.read_csv(path, encoding='utf-8')
print(type(dragon_data))
print(dragon_data.head())