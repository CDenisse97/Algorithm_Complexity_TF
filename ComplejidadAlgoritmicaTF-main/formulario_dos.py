!pip install pandas
!pip install networkx
!pip install graphviz
!apt-get install -y graphviz

import pandas as pd
import networkx as nx
import graphviz as gv
import random

class UFDS:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1

class Aplicacion:
    def __init__(self):
        self.df = None
        self.Categoria = ("Hotel", "Hostal", "Hospedaje")
        self.Establecimientos = []
        self.Grafo = None

        self.cargarDatos()
        self.crearGrafo()
        self.mostrarFormulario()

    def cargarDatos(self):
        self.df = pd.read_csv("/establecimiento.csv", sep=';', comment='#', encoding='utf-8')

    def crearGrafo(self):
        self.Grafo = nx.Graph()

    def aceptar(self):
        distrito = input("Ingrese el distrito: ")
        costo_inicial = int(input("Ingrese el costo inicial: "))
        costo_final = int(input("Ingrese el costo final: "))

        filtrado = self.df[(self.df["Distrito"] == distrito) & (self.df["Costo"] >= costo_inicial) & (self.df["Costo"] <= costo_final)]

        # Mostrar resultados
        if len(filtrado) > 0:
            print("Establecimientos encontrados:")
            for i, row in filtrado.iterrows():
                print(f"Nombre: {row['Nombre']}, Categoría: {row['Categoria']}, Costo: {row['Costo']}")
        else:
            print("No se encontraron establecimientos que cumplan los criterios de búsqueda.")

    def mostrarFormulario(self):
        print("Bienvenido al sistema de búsqueda de establecimientos")
        print("--------------------------------------------------")
        self.aceptar()

Aplicacion()
