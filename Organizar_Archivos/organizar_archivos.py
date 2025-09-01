import os
from pathlib import Path
def organizar_por_extension(carpeta):
    path_dir = Path(carpeta)
    if not path_dir.is_dir():
        print(f"{carpeta} no es una carpeta válida.")
        return
    for archivo in path_dir.iterdir():
        if archivo.is_file():
            ext = archivo.suffix[1:].upper() # Obtengo la extension del archivo
            # Crear la carpeta por extension
            carpeta_destino = path_dir / ext 
            carpeta_destino.mkdir(exist_ok=True) 
            # Mover  a la nueva carpeta el archivo segun su extension
            carpeta_destino.rename(carpeta_destino / archivo.name)
           
        
ruta = print("Ingrese la ruta del directorio a organizar:")
organizar_por_extension(ruta)