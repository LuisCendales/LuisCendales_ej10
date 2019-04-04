import pandas as pd

archivo1=pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2008.txt", sep=";", header=None, names=["fecha","hora","c","d"],index_col=False)
archivo1["fecha"]=archivo1["fecha"].astype(str).str[:-8]
archivo1["hora"]=archivo1["hora"].astype(str).str[-8:]

archivo2=pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2009.txt", sep=";", header=None, names=["fecha","hora","c","d"],index_col=False)
archivo2["fecha"]=archivo2["fecha"].astype(str).str[:-8]
archivo2["hora"]=archivo2["hora"].astype(str).str[-8:]

archivo3=pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/FISI2029-201910/master/Seccion_1/Fourier/Datos/transacciones2010.txt", sep=";", header=None, names=["fecha","hora","c","d"],index_col=False)
archivo3["fecha"]=archivo3["fecha"].astype(str).str[:-8]
archivo3["hora"]=archivo3["hora"].astype(str).str[-8:]

holi=pd.concat([archivo1,archivo2,archivo3])

export_csv = holi.to_csv ('./datos.csv')