from PIL import Image

from compiler.features.general_features import GeneralFeatures

class ClaseTransformarDefault(GeneralFeatures):
    img_global = None

    def aplicar_transformacion_default(self, imagen_original, nueva_imagen, transformacion):
        """
        Aplica una transformación a una imagen.

        Args:
            imagen_original (str): Ruta de la imagen original.
            nueva_imagen (str): Ruta donde se guardará la imagen modificada.
            transformacion (str): Nombre de la transformacion a aplicar.
        """
        
        # Crear una copia de la imagen
        self.img_global = self.edicion_imagen(imagen_original)

        # Aplicar el filtro seleccionado
        img_copia = self.transformacion_default[transformacion](self.img_global)

        # Guardar la imagen con el filtro aplicado
        self.guardar_imagen(img_copia, nueva_imagen)

    # Diccionario que relaciona nombres con filtros y sus respectivas funciones
    transformacion_default = {
        'flip_horizontally': lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),
        'flip_vertically': lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),
    }
