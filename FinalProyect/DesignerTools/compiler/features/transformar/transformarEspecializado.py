from compiler.features.general_features import GeneralFeatures

class ClaseTransformarEspecializado(GeneralFeatures):
    img_global = None

    def aplicar_transformacion_especializada(self, imagen_original, nueva_imagen, transformacion, *args):
        """
        Aplica una transformación a una imagen.

        Args:
            imagen_original (str): Ruta de la imagen original.
            nueva_imagen (str): Ruta donde se guardará la imagen modificada.
            transformacion (str): Nombre de la transformacion a aplicar.
            *args: Argumentos adicionales para la transformación.
        """
        
        # Crear una copia de la imagen
        self.img_global = self.edicion_imagen(imagen_original)

        # Diccionario que relaciona nombres con filtros y sus respectivas funciones
        transformacion_especializada = {
            'rotate': self.rotar_imagen,
            'crop': self.recortar_imagen,
        }
        # Aplicar el filtro seleccionado
        img_copia = transformacion_especializada[transformacion](imagen_original, nueva_imagen, *args)

        # Guardar la imagen con el filtro aplicado
        self.guardar_imagen(img_copia, nueva_imagen)

    def rotar_imagen(self, ruta_imagen, nombre_archivo, angulo):
        """
        Rota una imagen por el ángulo especificado y la guarda.

        Args:
            ruta_imagen (str): Ruta de la imagen a rotar.
            angulo (float): Ángulo de rotación.
            nombre_archivo (str): Nombre del archivo para guardar la imagen rotada.
        """
        try:
            angulo = float(angulo)
        except:
            raise ValueError("DesignerTools: El ángulo de rotación debe ser un único float")
        img = self.abrir_imagen(ruta_imagen)
        return img.rotate(angulo)

    def redimensionar_imagen(self, ruta_imagen, nombre_archivo, nuevo_tamano):
        """
        Redimensiona una imagen al tamaño especificado y la guarda.

        Args:
            ruta_imagen (str): Ruta de la imagen a redimensionar.
            nuevo_tamano (tuple): Nuevo tamaño (ancho, alto).
            nombre_archivo (str): Nombre del archivo para guardar la imagen redimensionada.
        """
        img = self.abrir_imagen(ruta_imagen)
        return img.resize(nuevo_tamano)
    
    def recortar_imagen(self, ruta_imagen, nombre_archivo, coordenadas):
        """
        Recorta una imagen según las coordenadas especificadas y la guarda.

        Args:
            ruta_imagen (str): Ruta de la imagen a recortar.
            coordenadas (tuple): Coordenadas de recorte (x1, y1, x2, y2).
            nombre_archivo (str): Nombre del archivo para guardar la imagen recortada.
        """
        img = self.abrir_imagen(ruta_imagen)
        return img.crop(coordenadas)