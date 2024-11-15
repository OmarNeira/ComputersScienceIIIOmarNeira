from compiler.features.mejorar.mejorarEspecializada import MejoraEspecializada as mejorarEspecializada

class Mejorar:
    mejoras_Generales={
        'brillo': "especializado",
        'contraste': "especializado",
        'color': "especializado",
        'nitidez': "especializado",
    }
    def aplicar_mejora(self, imagen_original, nueva_imagen, nombre_mejora, *args):
        """
        Aplica una mejora personalizada a una imagen.

        Args:
            imagen_original (str): Ruta de la imagen original.
            nueva_imagen (str): Ruta donde se guardará la imagen modificada.
            nombre_mejora (str): Nombre de la mejora a aplicar.
        """
        try:
            tipo_filtro = self.mejoras_Generales[nombre_mejora]
        except:
            print("Mejora no encontrado en la lista de mejoras generales")
            return
        #Creamos objeto de mejoraEspecializada
        if(tipo_filtro == "especializado"):
            #Creamos objeto de filtroColor
            mejoraObj = mejorarEspecializada()
            mejoraObj.aplicar_mejora_especializada(imagen_original, nueva_imagen, nombre_mejora, *args)

    