from compiler.features.filtro.filtroColor import FiltroColor as filtroColor
from compiler.features.filtro.filtroDefault import FiltroDefault as filtroDefault
from compiler.features.filtro.filtroEspecializado import FiltroEspecializado as filtroEspecializado

class ClaseFiltros:
    # Diccionario que relaciona nombres con filtros y sus valores RGB
    filtros_generales = {
        'sepia': "color",
        'negativo': "color",
        'blanco_negro': "color",
        'brillo': "color",
        'oscuro': "color",
        'rojo': "color",
        'verde': "color",
        'azul': "color",
        'desenfoque': "default",
        'contorno': "default",
        'detalles': "default",
        'borde': "default",
        'encontrar_bordes': "default",
        'suavizar': "default",
        'nitidez': "default",
        'desenfoque_gaussiano': "default",
        'escala_grises': "default",
        'relieve': "default",
        'nitidez': "default",
        'desenfoque_gaussiano': "especializado",
        #'ruido': "especializado",
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
            colorObj.aplicar_filtro_color(imagen_original, nueva_imagen, nombre_filtro)
        if(tipo_filtro == "default"):
            #Creamos objeto de filtroColor
            defaultObj = filtroDefault()
            defaultObj.aplicar_filtro_default(imagen_original, nueva_imagen, nombre_filtro)
        if(tipo_filtro == "especializado"):
            #Creamos objeto de filtroColor
            defaultObj = filtroEspecializado()
            defaultObj.aplicar_filtro_especializado(imagen_original, nueva_imagen, nombre_filtro, *args)