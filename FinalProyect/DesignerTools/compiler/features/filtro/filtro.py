from compiler.features.filtro.filtroColor import FiltroColor as filtroColor
from compiler.features.filtro.filtroDefault import FiltroDefault as filtroDefault
from compiler.features.filtro.filtroEspecializado import FiltroEspecializado as filtroEspecializado

class ClaseFiltros:
    # Diccionario que relaciona nombres con filtros y sus valores RGB
    filtros_generales = {
        'sepia': "color",
        'negative': "color",
        'black_white': "color",
        'dark': "color",
        'red': "color",
        'green': "color",
        'blue': "color",
        'blur': "default",
        'contour': "default",
        'detail': "default",
        'edge': "default",
        'find_edges': "default",
        'smooth': "default",
        'sharpen': "default",
        'grayscale': "default",
        'emboss': "default",
        'blur_gaussian': "especializado",
    }
    
    def aplicar_filtro(self, imagen_original, nueva_imagen, nombre_filtro, *args):
        """
        Aplica un filtro personalizado a una imagen basado en valores RGB.

        Args:
            imagen_original (str): Ruta de la imagen original.
            nueva_imagen (str): Ruta donde se guardará la imagen modificada.
            nombre_filtro (str): Nombre del filtro a aplicar.
        """
        try:
            tipo_filtro = self.filtros_generales[nombre_filtro]
        except:
            print("Filtro no encontrado en la lista de filtros generales")
            return
        #if else para relacionar el tipo_filtro con su clase
        if(tipo_filtro == "color"):
            #Creamos objeto de filtroColor
            colorObj = filtroColor()
            print(imagen_original," ", nueva_imagen," ", nombre_filtro)
            colorObj.aplicar_filtro_color(imagen_original, nueva_imagen, nombre_filtro)
        if(tipo_filtro == "default"):
            #Creamos objeto de filtroColor
            defaultObj = filtroDefault()
            defaultObj.aplicar_filtro_default(imagen_original, nueva_imagen, nombre_filtro)
        if(tipo_filtro == "especializado"):
            #Creamos objeto de filtroColor
            defaultObj = filtroEspecializado()
            defaultObj.aplicar_filtro_especializado(imagen_original, nueva_imagen, nombre_filtro, *args)