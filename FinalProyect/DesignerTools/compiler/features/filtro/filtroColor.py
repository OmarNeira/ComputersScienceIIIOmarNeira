from PIL import Image
from compiler.features.general_features import GeneralFeatures

class FiltroColor(GeneralFeatures):
    filtros_colores = {
        'sepia': [0.393, 0.769, 0.189],
        'negative': None,  # Ajustado para aplicar 255 - valor
        'black_white': [0.3, 0.59, 0.11],  # Valores de escala de grises
        'dark': [0.8, 0.8, 0.8],  # Ajustado para oscurecimiento leve
        'red': [1.0, 0.0, 0.0],
        'green': [0.0, 1.0, 0.0],
        'blue': [0.0, 0.0, 1.0],
    }
    
    def aplicar_filtro_color(self, imagen_original, nueva_imagen, nombre_filtro):
        """
        Aplica un filtro personalizado a una imagen basado en valores RGB.

        Args:
            imagen_original (str): Ruta de la imagen original.
            nueva_imagen (str): Ruta donde se guardará la imagen modificada.
            nombre_filtro (str): Nombre del filtro a aplicar
        """
        # Crear una copia de la imagen
        img_copia = self.edicion_imagen(imagen_original)
        
        # Convertir la imagen a modo RGB (si es necesario)
        img_copia = img_copia.convert('RGB')

        rgb = self.filtros_colores[nombre_filtro]

        if nombre_filtro == 'negative':
            # Para el filtro negativo, invertimos cada canal (255 - valor)
            img_custom = img_copia.point(lambda i: 255 - i)
        
        elif nombre_filtro == 'black_white':
            # Convertir a escala de grises aplicando los valores de ponderación
            img_custom = self.blanco_negro(img_copia,rgb)
        else:
            # Otros filtros aplican multiplicación simple a cada canal
            img_custom = self.cambiar_color(img_copia,rgb)

        # Guardar la imagen con el filtro personalizado
        self.guardar_imagen(img_custom, nueva_imagen)

    #Funcion que cambia colores a una imagen
    def cambiar_color(self, imagen, rgb):
        r, g, b = imagen.split()
        r = r.point(lambda i: min(i * rgb[0], 255))
        g = g.point(lambda i: min(i * rgb[1], 255))
        b = b.point(lambda i: min(i * rgb[2], 255))
        return Image.merge('RGB', (r, g, b))
    
    #Funcion que aplica un filtro de blanco y negro en una imagen
    def blanco_negro(self, imagen, rgb):
        imagen_custom = self.cambiar_color(imagen, rgb)
        r, g, b = imagen_custom.split()
        imagen_custom = Image.merge('RGB', (r, g, b)).convert('L').convert('RGB')
        return imagen_custom