from PIL import Image

from compiler.features.general_features import GeneralFeatures

class FiltroColor(GeneralFeatures):
    filtros_colores = {
        'sepia': [0.393, 0.769, 0.189],
        'negativo': [-1.0, -1.0, -1.0],
        'blanco_negro': [0.3, 0.59, 0.11],
        'brillo': [1.5, 1.5, 1.5],
        'oscuro': [0.5, 0.5, 0.5],
        'rojo': [1.0, 0.0, 0.0],
        'verde': [0.0, 1.0, 0.0],
        'azul': [0.0, 0.0, 1.0],
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

        # Obtener los canales de color
        r, g, b = img_copia.split()

        # Obtener los valores RGB del filtro
        rgb = self.filtros_colores[nombre_filtro]

        # Aplicar el filtro personalizado
        r = r.point(lambda i: i * rgb[0])
        g = g.point(lambda i: i * rgb[1])
        b = b.point(lambda i: i * rgb[2])

        # Combinar los canales de nuevo
        img_custom = Image.merge('RGB', (r, g, b))

        # Guardar la imagen con el filtro personalizado
        self.guardar_imagen(img_custom, nueva_imagen)