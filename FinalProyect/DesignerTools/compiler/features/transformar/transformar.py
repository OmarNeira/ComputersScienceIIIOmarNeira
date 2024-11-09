from compiler.features.transformar.transformarDefault import ClaseTransformarDefault as transformarDefault
from compiler.features.transformar.transformarEspecializado import ClaseTransformarEspecializado as transformarEspecializado

class ClaseTransformar:
    # Diccionario que relaciona nombres con filtros y sus valores RGB
    transformacion_generales = {
        'rotar': "especializada",
        'recortar': "especializada",
        'voltear_horizontal': "default",
        'voltear_vertical': "default",
    }
    
    def aplicar_transformacion(self, imagen_original, nueva_imagen, nombre_transformacion, *args):
        """
        Aplica una transformación personalizada a una imagen.

        Args:
            imagen_original (str): Ruta de la imagen original.
            nueva_imagen (str): Ruta donde se guardará la imagen modificada.
            nombre_transformacion (str): Nombre de la transformación a aplicar.
            *args: Argumentos adicionales para la transformación.
        """
        try:
            tipo_transformacion = self.transformacion_generales[nombre_transformacion]
        except:
            print("Transformación no encontrada en la lista de transformaciones generales")
            return
        #if else para relacionar el tipo_transformacion con su clase
        if(tipo_transformacion == "default"):
            #Creamos objeto de filtroColor
            transformacionDefaultObj = transformarDefault()
            transformacionDefaultObj.aplicar_transformacion_default(imagen_original, nueva_imagen, nombre_transformacion)
        if(tipo_transformacion == "especializada"):
            #Creamos objeto de filtroColor
            transformacionEspecializadoObj = transformarEspecializado()
            transformacionEspecializadoObj.aplicar_transformacion_especializada(imagen_original, nueva_imagen, nombre_transformacion, *args)