from PIL import ImageFilter

from compiler.features.general_features import GeneralFeatures

class FiltroDefault(GeneralFeatures):
    
    img_global = None

    def aplicar_filtro_default(self, imagen_original, nueva_imagen, filtro):
        """
        Aplica un filtro de desenfoque a una imagen.

        Args:
            imagen_original (str): Ruta de la imagen original.
            nueva_imagen (str): Ruta donde se guardará la imagen modificada.
            filtro (str): Nombre del filtro a aplicar.
        """
        
        # Crear una copia de la imagen
        self.img_global = self.edicion_imagen(imagen_original)

        # Aplicar el filtro seleccionado
        img_copia = self.filtros_default[filtro](self.img_global)

        # Guardar la imagen con el filtro aplicado
        self.guardar_imagen(img_copia, nueva_imagen)

    # Diccionario que relaciona nombres con filtros y sus respectivas funciones
    filtros_default = {
        'desenfoque': lambda img: img.filter(ImageFilter.BLUR),
        'contorno': lambda img: img.filter(ImageFilter.CONTOUR),
        'detalles': lambda img: img.filter(ImageFilter.DETAIL),
        'borde': lambda img: img.filter(ImageFilter.EDGE_ENHANCE),
        'encontrar_bordes': lambda img: img.filter(ImageFilter.FIND_EDGES),
        'suavizar': lambda img: img.filter(ImageFilter.SMOOTH),
        'escala_grises': lambda img: img.convert('L'),
        'relieve': lambda img: img.filter(ImageFilter.EMBOSS),
        'nitidez': lambda img: img.filter(ImageFilter.SHARPEN),
        'desenfoque_gaussiano': lambda img: img.filter(ImageFilter.GaussianBlur(radius=2)),
    }