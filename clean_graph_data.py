import pandas as pd
import networkx as nx

def clean_graph(file):
    df = pd.read_csv(file)

    #Eliminar valores nulos
    df = df.dropna()

    #Eliminar duplicados
    df = df.drop_duplicates()

    return df

if __name__ == "__main__":
    data = clean_graph("data.csv")
    print(data.head())
    print("Graph cleaning module loaded")