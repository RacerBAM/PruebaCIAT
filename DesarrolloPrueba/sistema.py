# Victor Manchola

# Se asumieron que las bases de datos son JSON
import json

# RECORDAR ESTRUCTURA DE LAS BASES DE DATOS:
# Ubicación de los animales
# - id
# - Latitud
# - Longitud
# - Propietario de los animales
# Zonas de deforestación
# - id
# - Latitud
# - Longitud
# - Area de Deforestacion
#    Este siempre es un string tipo "NUMEROxNUMERO"
# - Cambio de Cobertura



# LOS ARCHIVOS JSON, LAS BASES DE DATOS
archivo1 = "ubicacion_animales.json"
archivo2 = "zonas_deforestacion.json"

# LEYENDO LAS BASES DE DATOS A LISTAS PYTHON
with open(archivo1) as f:
    data_animales = json.load(f)
#print(data_animales)
da = json.dumps(data_animales, indent=1)
#print(da)

with open(archivo2) as f:
    data_zonas = json.load(f)
#print(data_zonas)
dz = json.dumps(data_zonas, indent=1)
#print(dz)



def animal_en_zonas(idanimal):
    """
Verifica si el animal dado esta en una zona de deforestacion.
Si lo esta, retorna el ID de las zonas.
De lo contrario, retorna una lista vacia.
Entradas: 1 entero
 Salidas: Una lista Python
    """
    global data_animales, data_zonas
    salida = []
    # Sacando LATITTUD y LONGITUD del animal consultado
    # Busqueda de animales no es muy eficiente
    for a in data_animales:
        if a["idanimal"] == idanimal:
            animal = a
            break
    animal_latitud  = animal["latitud"]
    animal_longitud = animal["longitud"]
    # Buscando las zonas en las cuales esta el animal
    for zona in data_zonas:
        # Toma STRING de AREA de NUMEROxNUMERO
        # y lo divide en los 2 numeros
        lista_area = zona["area"].split("x")
        a0 = int(lista_area[0])
        a1 = int(lista_area[1])
        zona_latitud  = zona["latitud"]
        zona_longitud = zona["longitud"]
        # Si el animal esta dentro de las longitudes y
        # latitudes de la zona, se reporta en la salida!
        if zona_latitud <= animal_latitud:
            if zona_longitud <= animal_longitud:
                if zona_latitud*a0 >= animal_latitud:
                    if zona_longitud*a1 >= animal_longitud:
                        salida.append(zona)
    return salida



def main():
    """
Programa principal e interfaz.
    """
    global data_animales, data_zonas
    print("Sistema para detectar animales en zonas de deforestacion.")
    print("Detectar animales en zonas?")
    print("1- Si.")
    print("2- No.")
    respuesta = int(input(">"))
    print()
    if respuesta == 1:
        for animal in data_animales:
            id = animal["idanimal"]
            lista_zonas = animal_en_zonas(id)
            print("El animal",id,"esta en esta(s) zona(s):")
            print(lista_zonas)
            print()
        print("Al recibir input, se cerrara el programa.")
        respuesta = input(">")
    else:
        print("Terminando...")
    quit()

main()


























    
