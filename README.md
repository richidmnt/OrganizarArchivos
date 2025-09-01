# Script: Organizar Archivos por Extensión

## Descripción
Este script en Python permite **organizar los archivos de una carpeta** creando subcarpetas según su extensión.  
Es ideal para mantener tu carpeta de documentos limpia y ordenada automáticamente.

Por ejemplo, si tienes archivos `.pdf`, `.docx` y `.xlsx`, el script creará carpetas `PDF`, `DOCX` y `XLSX` y moverá cada archivo a la carpeta correspondiente.

---

## Tecnologías
- Python 3.x
- Librerías estándar: `os`, `pathlib`

---

## Funcionalidades
- Detecta todos los archivos en la carpeta indicada.
- Crea subcarpetas por cada extensión de archivo (en mayúsculas).
- Mueve cada archivo a su carpeta correspondiente.
- Evita errores si la carpeta ya existe (`exist_ok=True`).

---

## Cómo usarlo

1. Clona o descarga el repositorio.  
2. Ejecuta el script desde tu terminal o IDE:
3.Ingrese la ruta del directorio a organizar:C:/Users/Admin/Documents

##Ejemplo de estructura
## Antes de ejecutar el script
Documents/
├─ archivo1.pdf
├─ archivo2.docx
├─ datos.xlsx

##Después de ejecutar el script
Documents/
├─ PDF/
│  └─ archivo1.pdf
├─ DOCX/
│  └─ archivo2.docx
├─ XLSX/
│  └─ datos.xlsx



