"""
GRAMMAR:
<S>              -> "START" <block> "END"
<block>          -> "START_OP" <statement> "END_OP" <block> | λ
<statement>      -> <image> <operation_type> <operation> | <folder> <operation_type> <operation>
<operation_type> -> "FILTER" | "TRANSFORM" | "ENHANCE"
<operation>      -> <filter> | <s_filter> | <transform> | <s_transform> | <s_enhance>
<filter>         -> "sepia" | "negative" | "black_white" | "dark" | "red" | "green" | "blue" | "blur" | "contour" | "detail" | "edge" | "find_edges" | "smooth" | "sharpen" | "grayscale" | "emboss
<s_filter>       -> "blur_gaussian" <number>
<transform>      -> "flip_horizontally" | "flip_vertically" | "rotate"
<s_transform>    -> "rotate" <number>
<s_enhance>      -> "brightness" <number> | "contrast" <number> | "color_enhance" <number> | "definition" <number>
<number>         -> -?\d+(\.\d+)?
<image>          -> "IMAGE("<IMAGE_URL>")"
<folder>         -> "FOLDER("<FOLDER_URL>")"
"""

class SintacticAnalyzer:
    """This class represents the behavior of a syntactic analyzer."""
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.pos = -1
        self.advance()

    def advance(self):
        """This method advances the current token
        to the next token."""
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]
        else:
            self.current_token = None

    def parse(self):
        """This method starts the parsing process.
        This just follows the structure of the grammar."""
        self.start()
        self.block()
        self.end()

    def start(self):
        """This method checks if the first token is 'START'."""
        if self.current_token.value == 'START':
            self.advance()
        else:
            self.error('START')

    def end(self):
        """This method checks if the last token is 'END'."""
        if self.current_token.value == 'END':
            self.advance()
            if self.current_token is not None:
                self.error('END')
        else:
            self.error('END')

    def block(self):
        """This method continues the parsing process.
        This just follows the structure of the grammar."""
        self.start_op()
        self.statement()
        self.end_op()
        if self.current_token and self.current_token.value == 'START_OP': # This is the recursive part of the grammar
            print("Recursive block")
            self.block()

    def start_op(self):
        """This method checks if the first token is 'START_OP'."""
        if self.current_token.value == 'START_OP':
            self.advance()
        else:
            self.error('START_OP')

    def end_op(self):
        """This method checks if the last token is 'END_OP'."""
        if self.current_token.value == 'END_OP':
            self.advance()
        else:
            self.error('END_OP')

    def statement(self):
        """This method checks if the sequence of a block of code is correct."""
        # Expecting <image><operation> | <folder><operation>
        if self.current_token.value == 'IMAGE' or self.current_token.value == 'FOLDER':
            self.advance()
            if self.current_token.type_ == 'URL':
                self.advance()
            else:
                self.error('URL of '+self.current_token.value)
        else:
            self.error('IMAGE or FOLDER')
        self.operation()
    
    def operation(self):
        """This method checks if the operation is correct."""
        # Expecting <filter> | <s_filter> | <transform> | <s_transform> | <s_enhance>
        if self.current_token.value == 'FILTER':
            self.advance()
            self.filter()
        elif self.current_token.value == 'TRANSFORM':
            self.advance()
            self.transform()
        elif self.current_token.value == 'ENHANCE':
            self.advance()
            self.enhance()
        else:
            self.error('FILTER, TRANSFORM or ENHANCE')
        
    def filter(self):
        """This method checks if the filter is correct."""
        # Expecting "sepia" | "negative" | "black_white" | "dark" | "red" | "green" | "blue" | "blur" | "contour" | "detail" | "edge" | "find_edges" | "smooth" | "sharpen" | "grayscale" | "emboss"
        if self.current_token.value in ['sepia', 'negative', 'black_white', 'dark', 'red', 'green', 'blue', 'blur', 'contour', 'detail', 'edge', 'find_edges', 'smooth', 'sharpen', 'grayscale', 'emboss']:
            self.advance()
        elif self.current_token.value == 'blur_gaussian':
            self.advance()
            self.s_filter()
        else:
            self.error('FILTER_NAME')
    
    def s_filter(self):
        """This method checks if the special_filter is correct."""
        if self.current_token.type_ == 'NUMBER':
            self.advance()
        else:
            self.error('NUMBER')

    def enhance(self):
        """This method checks if the enhance is correct."""
        # Expecting "brightness" | "contrast" | "color_enhance" | "definition"
        if self.current_token.value in ['brightness', 'contrast', 'color_enhance', 'definition']:
            self.advance()
            self.s_enhance()
        else:
            self.error('ENHANCE_NAME')

    def s_enhance(self):
        """This method checks if the special_enhance is correct."""
        if self.current_token.type_ == 'NUMBER':
            self.advance()
        else:
            self.error('NUMBER')

    def transform(self):
        """This method checks if the transform is correct."""
        # Expecting "flip_horizontally" | "flip_vertically" | "rotate" | "crop"
        if self.current_token.value in ['flip_horizontally', 'flip_vertically']: # Crop not supported yet
            self.advance()
        elif self.current_token.value == 'rotate': # or self.current_token.value == 'crop':
            self.advance()
            self.s_transform()
        else:
            self.error('TRANSFORM_NAME')

    def s_transform(self):
        """This method checks if the special_transform is correct."""
        if self.current_token.type_ == 'NUMBER':
            self.advance()
        else:
            self.error('NUMBER')

    def error(self, expected):
        """This method raises an exception if the current token is not the expected one.
        
        Args:
            expected (str): The expected token.
        """
        raise Exception(f"Designer Tools syntax error: expected {expected}, found {self.current_token}")