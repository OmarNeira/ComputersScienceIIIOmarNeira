#Analizer imports
from compiler.input_analizer.lexical_analizer.lexical import LexicalAnalyzer
from compiler.input_analizer.sintactic_analizer.sintactic import SintacticAnalyzer
from compiler.input_analizer.semantic_analizer.semantic import SemanticAnalyzer

#Features imports
import os
from compiler.features.filtro.filtro import ClaseFiltros as Filtro
from compiler.features.transformar.transformar import ClaseTransformar as Transformar
from compiler.features.mejorar.mejorar import Mejorar as Mejorar
from compiler.features.general_features import GeneralFeatures as general

from compiler.paths.paths import Paths as Paths

"""
# Use example:
imagen_original = "common/img_resources/imagen.jpg"
nueva_imagen = "common/img_export/imagen_editada.jpg"  # Incluye el nombre del archivo en la ruta

carpeta_original = "common/img_resources/"
nueva_carpeta = "common/img_export/"

# Crear los directorios si no existen
os.makedirs(os.path.dirname(nueva_imagen), exist_ok=True)

# Crear instancias de las clases
filtroObj = Filtro()
transformarObj = Transformar()
mejorarObj = Mejorar()
generalObj = general()

# Crear instancias de clase path
pathObj = Paths()

# Aplicar el filtro a cada imagen en el path
for imagen_seleccionada in pathObj.pathsImagenes(carpeta_original):
    filtroObj.aplicar_filtro(imagen_seleccionada, pathObj.pathsImagenesEditadas(imagen_seleccionada,nueva_carpeta), "smooth", 3)
    #mejorarObj.aplicar_mejora(imagen_seleccionada, pathObj.pathsImagenesEditadas(imagen_seleccionada,nueva_carpeta), "contraste", 10)

#Transformar la imagen
#transformarObj.aplicar_transformacion(imagen_original, nueva_imagen, "recortar", (100, 100, 400, 400))

# Muestra la imagen
for export_imagen in pathObj.pathsImagenes(nueva_carpeta):
    generalObj.mostrar_imagen(export_imagen)
"""

class Compiler:
    # Crear instancias de clase path
    pathObj = Paths()
    # Default folder for the edited images
    nueva_carpeta = "common/img_export/"
    """This class represents the behavior of a complete compiler."""
    def compile(self, code: str):
        """This method compiles the code."""
        tokens_ = LexicalAnalyzer.lex(code)
        print(tokens_)
        sintactic_analyzer = SintacticAnalyzer(tokens_)
        sintactic_analyzer.parse()
        semantic_analyzer_ = SemanticAnalyzer(tokens_)
        operations = semantic_analyzer_.analyze()
        #execute operations
        self.compile_operations(operations)
        #show results
        generalObj = general()
        # Muestra la imagen
        for export_imagen in self.pathObj.pathsImagenes(self.nueva_carpeta):
            generalObj.mostrar_imagen(export_imagen)
    
    def compile_operations(self, operations: list):
        """This method executes the operations."""
        for operation in operations:
            print(operation)
            if operation[0].value == 'FOLDER':
                folder_token = operation[1]
                # Get the folder
                try:
                    # Get the folder without first and last character, those are "(" and ")"
                    folder = folder_token.value[1:-1]
                    images = self.pathObj.pathsImagenes(folder)
                except Exception as error:
                    raise RuntimeError("Designer tools, error getting the folder: ", error)
                # Run the operations
                for image in images:
                    self.run_image(image, operation)
            elif operation[0].value == 'IMAGE':
                image_token = operation[1]
                # Get the image
                try:
                    # Get the image without first and last character, those are "(" and ")"
                    image = image_token.value[1:-1]
                    self.pathObj.pathIsImage(image)
                except Exception as error:
                    raise RuntimeError("Designer tools, error getting the image: ", error)
                # Run the operations
                self.run_image(image, operation)
    
    # For each image in the folder, run the operations
    def run_image(self, image: str, operation: list):
        """This method runs the image."""
        print("longitud de la operacion: ",len(operation))
        if len(operation) > 4:  # Si hay argumentos extras
            print("Extra arguments for ",operation[3].value, operation[4].value)
            self.run_operator(image, operation[2].value, operation[3].value, operation[4].value)
        else:
            print("Not extra arguments")
            self.run_operator(image, operation[2].value, operation[3].value)
        pass

    def run_operator(self, image, operator: str, operation: str, args=None):
        print("Running operator: ", operator, " with operation: ", operation, " and args: ", args," to image ", image)
        # Create the references to the classes
        if 'FILTER' in operator:
            filtroObj = Filtro()
            print("Filtro")
            filtroObj.aplicar_filtro(image, self.pathObj.pathsImagenesEditadas(image,self.nueva_carpeta), operation, args)
        elif 'TRANSFORM' in operator:
            transformarObj = Transformar()
            transformarObj.aplicar_transformacion(image, self.pathObj.pathsImagenesEditadas(image,self.nueva_carpeta), operation, args)
        elif 'ENHANCE' in operator:
            mejorarObj = Mejorar()
            mejorarObj.aplicar_mejora(image, self.pathObj.pathsImagenesEditadas(image,self.nueva_carpeta), operation, args)
        
        """This method runs the operator."""
        pass
