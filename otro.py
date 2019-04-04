import pandas as pd
import matplotlib.pylab as plt
import os

os.system("python ejercicio.py")
f=pd.read_csv("datos.csv", sep=",")

plt.figure(figsize=(20,10))
plt.scatter(range(f.shape[0]),f["c"])
plt.savefig("fig.png")
plt.close()