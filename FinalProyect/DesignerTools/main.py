from comp import Compiler

# =========== Example usage ========== #
def example(compiler_: Compiler):
    """This function is an example of how to use the compiler."""
    input_text = r"""
    START
        START_OP
            TO_IMAGE (image.jpg)
            APPLY_FILTER sepia
        END_OP
        START_OP
            TO_FOLDER (example)
            APPLY_ENHANCE contrast 8
        END_OP
        START_OP
            TO_IMAGE (example/design.png)
            APPLY_TRANSFORM rotate 180
        END_OP
    END
    """
    compiler_.compile(input_text)

if __name__ == '__main__':
    compiler = Compiler()
    example(compiler)