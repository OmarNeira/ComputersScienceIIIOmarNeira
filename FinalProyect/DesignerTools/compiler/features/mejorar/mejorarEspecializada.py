from PIL import ImageEnhance

from compiler.features.general_features import GeneralFeatures

class MejoraEspecializada(GeneralFeatures):
    def aplicar_mejora_especializada(self, imagen_original, nueva_imagen, nombre_mejora, *args):
        """
        Aplica una mejora a una imagen.

        Args:
            imagen_original (str): Ruta de la imagen original.
            nueva_imagen (str): Ruta donde se guardará la imagen modificada.
            nombre_mejora (str): Nombre de la mejora a aplicar.
            *args: Argumentos adicionales para la mejora.
        """
        # Crear una copia de la imagen
        self.img_global = self.edicion_imagen(imagen_original)

        # Diccionario que relaciona nombres con mejoras y sus respectivas funciones
        mejora_especializada = {
            'brightness': self.brillo,
            'contrast': self.contraste,
            'color_enhance': self.color,
            'definition': self.nitidez,
        }

        # Aplicar la mejora seleccionada
        img_copia = mejora_especializada[nombre_mejora](imagen_original, nueva_imagen, *args)

        # Guardar la imagen con la mejora aplicada
        self.guardar_imagen(img_copia, nueva_imagen)
    
    # Funcion que aplica brillo a una imagen
    def brillo(self, imagen, nueva_imagen, *args):
        """
        Aplica brillo a una imagen.

        Args:
            imagen (Image): Imagen a la que se le aplicará el brillo.
            *args: Número decimal para el brillo.
        """
        # Verificar que el argumento es un decimal
        if not isinstance(args[0], float):
            try:
                args = (float(args[0]),)
            except:
                raise ValueError("El valor del brillo debe ser un decimal")

        brillo = args[0]
        img_copia = self.edicion_imagen(imagen)
        return ImageEnhance.Brightness(img_copia).enhance(brillo)
    
    # Funcion que aplica contraste a una imagen
    def contraste(self, imagen, nueva_imagen, *args):
        """
        Aplica contraste a una imagen.

        Args:
            imagen (Image): Imagen a la que se le aplicará el contraste.
            *args: Número decimal para el contraste.
        """
        # Verificar que el argumento es un decimal
        if not isinstance(args[0], float):
            try:
                args = (float(args[0]),)
            except:
                raise ValueError("El valor del contraste debe ser un decimal")

        contraste = args[0]
        img_copia = self.edicion_imagen(imagen)
        return ImageEnhance.Contrast(img_copia).enhance(contraste)
    
    # Funcion que aplica color a una imagen
    def color(self, imagen, nueva_imagen, *args):
        """
        Aplica color a una imagen.

        Args:
            imagen (Image): Imagen a la que se le aplicará el color.
            *args: Número decimal para el color.
        """
        # Verificar que el argumento es un decimal
        if not isinstance(args[0], float):
            try:
                args = (float(args[0]),)
            except:
                raise ValueError("El valor del color debe ser un decimal")

        color = args[0]
        img_copia = self.edicion_imagen(imagen)
        return ImageEnhance.Color(img_copia).enhance(color)
    
    # Funcion que aplica nitidez a una imagen
    def nitidez(self, imagen, nueva_imagen, *args):
        """
        Aplica nitidez a una imagen.

        Args:
            imagen (Image): Imagen a la que se le aplicará la nitidez.
            *args: Número decimal para la nitidez.
        """
        # Verificar que el argumento es un decimal
        if not isinstance(args[0], float):
            try:
                args = (float(args[0]),)
            except:
                raise ValueError("El valor de la nitidez debe ser un decimal")

        nitidez = args[0]
        img_copia = self.edicion_imagen(imagen)
        return ImageEnhance.Sharpness(img_copia).enhance(nitidez)