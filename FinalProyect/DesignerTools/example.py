from comp import Compiler

# =========== Example usage ========== #
def example(compiler_: Compiler):
    """This function is an example of how to use the compiler."""
    input_text = r"""
    START
    START_OP
    
    
    FOLDER (C:\Users\omarn\Documents\GitHub\ComputersScienceIIIOmarNeira\FinalProyect\DesignerTools\common\img_resources)
    
    FILTER sepia
    END_OP
    END
    """#SI EJECUTA AMBOS PERO SOBREESCRIBE LA SEGUNDA IMAGEN A LA PRIMERA
    compiler_.compile(input_text)

if __name__ == '__main__':
    compiler = Compiler()
    example(compiler)