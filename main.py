import csv
import json

ruta_csv = "./archivos/cities.csv"
ruta_json = "./archivos/cities.json"

#Funcion para leer y obtener la data del csv
def leer_csv(ruta):
    if(ruta[-4:]!=".csv"):
        print("No es un archivo .csv")
        return
    with open(ruta,"r") as file:
        reader = csv.DictReader(file, skipinitialspace=True) #almacena el contenido del csv como diccionario
        fields = reader.fieldnames #almacena las claves del diccionario
        data = [] 
        for row in reader:
            data.append({fields[i]:row[fields[i]] for i in range(len(fields))})
        escribir_json(data,ruta_json)

def escribir_json(data,ruta):
    with open(ruta, "w") as file:
        json.dump(data, file, indent=4)

leer_csv(ruta_csv)