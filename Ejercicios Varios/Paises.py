import requests
import pandas as pd
import gzip
from io import StringIO

# Descargar el archivo
url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true"
response = requests.get(url)

# Guardar el archivo descargado
with open('sdg_08_10.tsv.gz', 'wb') as f:
    f.write(response.content)

# Descomprimir el archivo y cargar los datos usando pandas
with gzip.open('sdg_08_10.tsv.gz', 'rb') as f:
    file_content = f.read()

# Decodificar los datos y leerlos con pandas
data = file_content.decode('utf-8')
df = pd.read_csv(StringIO(data), delimiter='\t')

# Pedir al usuario las iniciales del país
country_initials = input("Ingresa las iniciales del país en mayúsculas (por ejemplo, ES para España): ")

# Filtrar los datos para el país ingresado por el usuario
filtered_data = df[df['geo\\time'] == country_initials]

# Mostrar el PIB per cápita para el país ingresado por cada año disponible
if not filtered_data.empty:
    print(f"PIB per cápita para {country_initials}:")
    for index, row in filtered_data.iterrows():
        print(f"Año {row['time']}: {row['values']}")
else:
    print("No se encontraron datos para el país ingresado.")