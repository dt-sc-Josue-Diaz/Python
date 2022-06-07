# La ejecucion  en una terminal es `python3 codigo_prueba_tecnica.py` 

# Librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # para hacer gráficas
import seaborn as sns # para hacer gráficas mas bonitas que plt

#%matplotlib inline

# Importar datos, estamos importando un archivos csv
df_covid = pd.read_csv("datos.csv", encoding='latin-1')

# Nombre de las columnas
np.array(df_covid.columns).reshape(5,8)

# Eliminar las observaciones nulas
df_covid = df_covid.dropna()

# Vamos a hacer que la variable CLASIFICACION_FINAL sea una categorica
df_covid["TABAQUISMO"] = df_covid["TABAQUISMO"].astype("category")

# Deacuerdo a la página donde de obtienen los datos, 1,2 y 3 
# corresponden a casos registrados como defunciones
df_covid = df_covid[(df_covid.CLASIFICACION_FINAL == 1) | (df_covid.CLASIFICACION_FINAL == 2) | (df_covid.CLASIFICACION_FINAL == 3) ]
df_covid

# Las filas y las columnas de los filtros anteriores
df_covid.shape

# Vista previa de los datos
df_covid.head()

# Estadisticas básicas de los datos. Reconocer la situación de los datos.
df_covid.describe

# Matriz de correlación.
corrmat = df_covid.corr()

# mapa de calor
f, ax = plt.subplots(figsize = (12,9))
sns.heatmap(corrmat, vmax = .8, square = True)

data = pd.concat([df_covid["FECHA_SINTOMAS"],df_covid["EDAD"]], axis= 1)

data = data.sort_values('FECHA_SINTOMAS', ascending = True)

data.head()

data.plot.scatter(x = "FECHA_SINTOMAS" , y = "EDAD", ylim=(0,120))

# Vamos hacer un gráfico en dos variables.
var = "TABAQUISMO"
f, ax = plt.subplots(figsize = (10,10)) # subplot
fig = sns.boxplot(x = var, y = "EDAD", data = df_covid) # gráfico de caja
fig.axis(ymin=0,ymax=120) # los parametro del eje y