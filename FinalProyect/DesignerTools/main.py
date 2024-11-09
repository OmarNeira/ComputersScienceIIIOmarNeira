import os
from compiler.features.filtro.filtro import ClaseFiltros as Filtro
from compiler.features.transformar.transformar import ClaseTransformar as Transformar
from compiler.features.general_features import GeneralFeatures as general

# Ejemplo de uso:
imagen_original = "common/img_resources/imagen.jpg"
nueva_imagen = "common/img_export/imagen_editada.jpg"  # Incluye el nombre del archivo en la ruta

# Crear los directorios si no existen
os.makedirs(os.path.dirname(nueva_imagen), exist_ok=True)

# Crear instancias de las clases
filtroObj = Filtro()
transformarObj = Transformar()
generalObj = general()

# Aplicar el filtro
#filtroObj.aplicar_filtro(imagen_original, nueva_imagen, "relieve")

#Transformar la imagen
transformarObj.aplicar_transformacion(imagen_original, nueva_imagen, "recortar", (100, 100, 400, 400))

# Muestra la imagen
# visualizadorObj.abrir_imagen(imagen_original)
generalObj.mostrar_imagen(nueva_imagen)