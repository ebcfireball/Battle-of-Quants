import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_parquet('BOQ_data.parquet')
print(df.size)

def scatter_plot(x_label, y_label):
    plt.scatter(df[x_label], df[y_label])
    plt.xlabel('sale')
    plt.ylabel('beta')
    plt.legend()
    plt.show()

