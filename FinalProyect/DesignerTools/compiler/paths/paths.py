import datetime
import os

#Formatos de archivo permitidos por pillow
formatos_permitidos = ['bmp', 'dib', 'eps', 'gif', 'icns', 'ico', 'im', 'jpeg', 'jpg', 'msp', 'pcx', 'png', 'ppm', 'sgi', 'spider', 'tiff', 'webp', 'xbm']

#Clase que se encarga de manejar los paths de las imagenes
class Paths:
    #Funcion que toma un path y devuelve el path de cada imagen
    def pathsImagenes(self, path):
        """
        Toma un path y devuelve el path de cada imagen.
        
        Args:
            path (str): Ruta de la carpeta que contiene las imágenes.
        
        Donde el path debe de terner un formato similar a:
        "common/img_resources/"
        """
        #Definimos un arreglo para guardar los paths
        paths = []
        #Recogemos cada uno de los archivos en el path
        for file in os.listdir(path):
            #Si el archivo es una imagen de los formatos permitidos
            if file.endswith(tuple(formatos_permitidos)):
                #Guardamos el path de la imagen
                paths.append(os.path.join(path, file))
        return paths

    #Funcion que toma un path y verifica si es una imagen de los formatos permitidos
    def pathIsImage(self, path):
        """
        Toma un path y verifica si es una imagen de los formatos permitidos.
        
        Args:
            path (str): Ruta de la imagen.
        """
        #Si el archivo es una imagen de los formatos permitidos
        if path.endswith(tuple(formatos_permitidos)):
            return True
        return False

    def get_path(self):
        return self.path
    
    #Funcion que toma un path y devuelve el path de cada imagen
    #Genera el nombre de la imagen editada con el formato "nombre_original_DD-MM-YYYY_HH-MM-SS-ffffff.formato"
    def pathsImagenesEditadas(self, path, nueva_carpeta=None):
        """
        Toma un path y devuelve el path de cada imagen.
        
        Args:
            path (str): Ruta de la carpeta que contiene las imágenes.
            nueva_carpeta (str): Ruta de la carpeta donde se guardarán las imágenes editadas.
        
        Donde el path y nueva_carpeta debe de tener un formato similar a:
        "common/img_resources/"
        "common/img_export/"

        nueva_carpeta es un argumento opcional, si no se proporciona, se usará el path original.
        """
        # Si nueva_carpeta está presente, path_original se iguala a nueva_carpeta
        if nueva_carpeta:
            path_original = nueva_carpeta
        else:
            # Tomamos el path de la imagen original
            path_original = path
        # Tomamos el nombre de la imagen original
        nombre_original = os.path.basename(path)
        # Tomamos la extensión de la imagen original
        extension = os.path.splitext(path)[1]
        # Tomamos la fecha y hora actual con microsegundos
        fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")
        # Generamos el nombre de la imagen editada
        nombre_editado = nombre_original.split(".")[0] + "_" + fecha_hora + extension
        # Generamos el path de la imagen editada
        
        path_editado = os.path.join(os.path.dirname(path_original), nombre_editado)
        return path_editado