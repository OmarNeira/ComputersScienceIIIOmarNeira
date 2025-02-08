import random
from PIL import ImageFilter

from compiler.features.general_features import GeneralFeatures

class FiltroEspecializado(GeneralFeatures):
    def aplicar_filtro_especializado(self, imagen_original, nueva_imagen, filtro, *args):
        """
        Aplica un filtro a una imagen.

        Args:
            imagen_original (str): Ruta de la imagen original.
            nueva_imagen (str): Ruta donde se guardará la imagen modificada.
            filtro (str): Nombre del filtro a aplicar.
            *args: Argumentos adicionales para la transformación.
        """
        # Crear una copia de la imagen
        self.img_global = self.edicion_imagen(imagen_original)

        # Diccionario que relaciona nombres con filtros y sus respectivas funciones
        filtro_especializado = {
            #'ruido': self.agregar_ruido,
            'blur_gaussian': self.desenfoque_gaussiano,	
        }

        # Aplicar el filtro seleccionado
        img_copia = filtro_especializado[filtro](imagen_original, nueva_imagen, *args)

        # Guardar la imagen con el filtro aplicado
        self.guardar_imagen(img_copia, nueva_imagen)

    # Funcion que aplica el desenfoque gaussiano a una imagen
    def desenfoque_gaussiano(self, imagen, nueva_imagen, *args):
        """
        Aplica un filtro a una imagen.

        Args:
            imagen (Image): Imagen a la que se le aplicará el filtro.
            *args: Número entero para el radio de desenfoque gaussiano.
        """
        # Verificar que el argumento es un float convirtiendolo a float
        try:
            radio = float(*args)
        except:
            raise ValueError("DesignerTools: El valor del radio de desenfoque gaussiano debe ser un único float")

        img_copia = self.edicion_imagen(imagen)
        return img_copia.filter(ImageFilter.GaussianBlur(radius=radio))
    
    # Funcion que agrega ruido a una imagen usando un random
    # Funcion no soportada por la poca eficiencia, se propone utilizar numpy para optimizar
    # Pero no se agrega para evitar la instalacion de una libreria adicional
    def agregar_ruido(self, imagen, *args):
        """
        Aplica un filtro a una imagen.

        Args:
            imagen (Image): Imagen a la que se le aplicará el filtro.
            *args: Número entero para la cantidad de ruido.
        """
        # Verificar que el argumento es un entero
        if len(args) != 1 or not isinstance(args[0], int):
            raise ValueError("El valor del ruido debe ser un único entero")

        ruido_max = args[0]

        # Convertir la imagen a modo RGB si no lo está
        if imagen.mode != 'RGB':
            imagen = imagen.convert('RGB')

        pixels = imagen.load()
        width, height = imagen.size
        for i in range(width):
            for j in range(height):
                r, g, b = imagen.getpixel((i, j))
                noise = random.randint(-ruido_max, ruido_max)
                r = min(255, max(0, r + noise))
                g = min(255, max(0, g + noise))
                b = min(255, max(0, b + noise))
                pixels[i, j] = (r, g, b)
        return imagen