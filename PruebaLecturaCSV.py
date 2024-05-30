import pandas as pd

def read_csv(file_path):import pandas as pd

def read_csv(file_path):
    # Lista de países de la Unión Europea
    eu_countries = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Republic of Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']

    data = pd.read_csv(file_path)

    # Filtrar los datos para incluir solo los países de la Unión Europea
    eu_data = data[data['Country Name'].isin(eu_countries)]

    print(eu_data)

# Uso de la función
file_path = '/Users/pruebaprueba/Documents/ETSII/Tercero/Segundo Cuatrimestre/IA/Proyecto IA/Evaluacion-de-Riesgos-en-Proyectos-de-Desarrollo-de-Aplicaciones-Moviles/Porcentaje Individuos Con Acceso a Internet/ba49add3-1ef6-4d95-9e32-21d877473b59_Data.csv'
read_csv(file_path)
data = pd.read_csv(file_path)
print(data)

# Uso de la función
file_path = '/Users/pruebaprueba/Documents/ETSII/Tercero/Segundo Cuatrimestre/IA/Proyecto IA/Evaluacion-de-Riesgos-en-Proyectos-de-Desarrollo-de-Aplicaciones-Moviles/Porcentaje Individuos Con Acceso a Internet/ba49add3-1ef6-4d95-9e32-21d877473b59_Data.csv'
read_csv(file_path)
