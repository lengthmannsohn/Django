import json
import matplotlib.pyplot as plt

# JSON con los datos de distribución de ocupaciones en España
json_data = '''
{
  "labels": [
    "Directores y gerentes",
    "Técnicos y profesionales científicos e intelectuales",
    "Técnicos y profesionales de apoyo",
    "Empleados contables, administrativos y otros de oficina",
    "Camareros",
    "Dependientes de tiendas y almacenes",
    "Otros trabajadores de servicios y vendedores",
    "Trabajadores cualificados agrícolas, ganaderos, forestales y pesqueros",
    "Artesanos y trabajadores cualificados de industrias manufactureras y construcción",
    "Operadores de instalaciones y maquinaria, y montadores",
    "Trabajadores no cualificados"
  ],
  "datasets": [
    {
      "label": "Porcentaje de ocupados",
      "data": [
        2.5,
        19.8,
        10.7,
        8.9,
        6.2,
        5.8,
        5.6,
        4.0,
        11.5,
        6.3,
        12.7
      ]
    }
  ]
}
'''

# Convertir JSON a un diccionario de Python
data = json.loads(json_data)

# Extraer etiquetas y valores
labels = data["labels"]
values = data["datasets"][0]["data"]

# Crear la gráfica de barras
plt.figure(figsize=(12, 6))
plt.barh(labels[::-1], values[::-1], color='teal', edgecolor='black')

# Etiquetas y título
plt.xlabel("Porcentaje de ocupados")
plt.ylabel("Categorías profesionales")
plt.title("Distribución de la población ocupada en España por categorías profesionales (Q4 2024)")
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Mostrar la gráfica
plt.show()