import os
from compiler.features.filtro.filtro import ClaseFiltros as Filtro
from compiler.features.transformar.transformar import ClaseTransformar as Transformar
from compiler.features.mejorar.mejorar import Mejorar as Mejorar
from compiler.features.general_features import GeneralFeatures as general

from compiler.paths.paths import Paths as Paths

# Ejemplo de uso:
imagen_original = "common/img_resources/imagen.jpg"
nueva_imagen = "common/img_export/imagen_editada.jpg"  # Incluye el nombre del archivo en la ruta

carpeta_original = "common/img_resources/"
nueva_carpeta = "common/img_export/"

# Crear los directorios si no existen
os.makedirs(os.path.dirname(nueva_imagen), exist_ok=True)

# Crear instancias de las clases
filtroObj = Filtro()
transformarObj = Transformar()
mejorarObj = Mejorar()
generalObj = general()

# Crear instancias de clase path
pathObj = Paths()

# Aplicar el filtro a cada imagen en el path
for imagen_seleccionada in pathObj.pathsImagenes(carpeta_original):
    #filtroObj.aplicar_filtro(imagen_seleccionada, pathObj.pathsImagenesEditadas(imagen_seleccionada,nueva_carpeta), "desenfoque_gaussiano", 3)
    mejorarObj.aplicar_mejora(imagen_seleccionada, pathObj.pathsImagenesEditadas(imagen_seleccionada,nueva_carpeta), "contraste", 10)

#Transformar la imagen
#transformarObj.aplicar_transformacion(imagen_original, nueva_imagen, "recortar", (100, 100, 400, 400))

# Muestra la imagen
for export_imagen in pathObj.pathsImagenes(nueva_carpeta):
    generalObj.mostrar_imagen(export_imagen)