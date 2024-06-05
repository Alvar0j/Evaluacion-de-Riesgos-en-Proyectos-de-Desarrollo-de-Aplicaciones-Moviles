import sys
from pgmpy.models.BayesianModel import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Definir el modelo bayesiano
model = BayesianNetwork()

# Añadir nodos y aristas basadas en las relaciones de riesgos
model.add_edges_from([
    ("X1", "X2"),
    ("X1", "T1"),
    ("T2", "Z1"),
    ("Z1", "X1"),
    ("Y1", "Z2"),
    ("Y2", "Z2"),
    # Conectar todos los riesgos al riesgo del sistema
    ("X1", "Riesgo Sistema"),
    ("X2", "Riesgo Sistema"),
    ("Y1", "Riesgo Sistema"),
    ("Y2", "Riesgo Sistema"),
    ("Z1", "Riesgo Sistema"),
    ("Z2", "Riesgo Sistema"),
    ("T1", "Riesgo Sistema"),
    ("T2", "Riesgo Sistema")
])

# Definir las CPDs (probabilidades condicionales) de cada nodo
cpd_X1 = TabularCPD(variable='X1', variable_card=2, values=[[0.8], [0.2]])
cpd_X2 = TabularCPD(variable='X2', variable_card=2, values=[[0.7, 0.1], [0.3, 0.9]], evidence=['X1'], evidence_card=[2])
cpd_Y1 = TabularCPD(variable='Y1', variable_card=2, values=[[0.9], [0.1]])
cpd_Y2 = TabularCPD(variable='Y2', variable_card=2, values=[[0.85], [0.15]])
cpd_Z1 = TabularCPD(variable='Z1', variable_card=2, values=[[0.9, 0.4], [0.1, 0.6]], evidence=['T2'], evidence_card=[2])
cpd_Z2 = TabularCPD(variable='Z2', variable_card=2, values=[[0.8, 0.5, 0.3, 0.2], [0.2, 0.5, 0.7, 0.8]], evidence=['Y1', 'Y2'], evidence_card=[2, 2])
cpd_T1 = TabularCPD(variable='T1', variable_card=2, values=[[0.85, 0.5], [0.15, 0.5]], evidence=['X1'], evidence_card=[2])
cpd_T2 = TabularCPD(variable='T2', variable_card=2, values=[[0.7], [0.3]])

# Crear una matriz de probabilidades para 'Riesgo Sistema' con el tamaño correcto
values = np.zeros((2, 256))
values[0] = np.linspace(0.99, 0.01, 256)
values[1] = 1 - values[0]

cpd_riesgo_sistema = TabularCPD(
    variable='Riesgo Sistema', variable_card=2, values=values,
    evidence=['X1', 'X2', 'Y1', 'Y2', 'Z1', 'Z2', 'T1', 'T2'],
    evidence_card=[2, 2, 2, 2, 2, 2, 2, 2]
)

# Añadir las CPDs al modelo
model.add_cpds(cpd_X1, cpd_X2, cpd_Y1, cpd_Y2, cpd_Z1, cpd_Z2, cpd_T1, cpd_T2, cpd_riesgo_sistema)

# Comprobar si el modelo está correctamente definido
assert model.check_model()

# Realizar inferencia sobre el modelo
inference = VariableElimination(model)

# Ejemplo de consulta: ¿Cuál es la probabilidad del riesgo del sistema si X1 ocurre?
query_result = inference.query(variables=['Riesgo Sistema'], evidence={'X1': 1})
print(query_result)

# Visualizar la red bayesiana usando networkx y matplotlib
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(model)
nx.draw(model, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20, edge_color="gray")
plt.title("Modelo Bow-Tie de los Riesgos del Proyecto")
plt.show()
