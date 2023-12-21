import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana'],
    'Edad': [25, 30, 22, 28],
    'Ciudad': ['Barcelona', 'Madrid', 'Sevilla', 'Valencia']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)
