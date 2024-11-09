from PIL import Image
import os

class GeneralFeatures:
    """
    Clase con funciones generales para el manejo de imágenes.
    """
    #Funcion para abrir imagen
    def abrir_imagen(self, ruta_imagen):
        """
        Abre una imagen desde la ruta especificada.

        Args:
            ruta_imagen (str): Ruta de la imagen a abrir.

        Returns:
            Image: Objeto de imagen abierto.
        """
        return Image.open(ruta_imagen)

    def edicion_imagen(self, ruta_img):
       """
        Abre una imagen y retorna una copia para edicion.

        Args:
            img (Image): Objeto de imagen a guardar.
        """
       img = Image.open(ruta_img)
       img = img.copy()
       return img

    #Funcion para guardar imagen
    def guardar_imagen(self, img, ruta_guardar):
        """
        Guarda una imagen en la ruta especificada.

        Args:
            img (Image): Objeto de imagen a guardar.
            ruta_guardar (str): Ruta donde se guardará la imagen.
        """
        os.makedirs(os.path.dirname(ruta_guardar), exist_ok=True)
        img.save(ruta_guardar)

    #Funcion para mostrar imagen
    def mostrar_imagen(self, ruta_imagen):
        """
        Muestra una imagen en una ventana emergente.

        Args:
            img (Image): Objeto de imagen a mostrar.
        """
        img = Image.open(ruta_imagen)
        img.show()