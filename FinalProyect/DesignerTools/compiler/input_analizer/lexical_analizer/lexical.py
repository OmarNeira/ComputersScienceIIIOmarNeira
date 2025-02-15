import re

class Token:
    """This class represents the data structure of a token.
    It means: a type of token and its value (lexema)."""
    def __init__(self, type_: str, value):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type_}, {self.value})"

class LexicalAnalyzer:
    """This class represents the behavior of a lexical analyzer."""

    @staticmethod
    def lex(code):
        """This method receives a code and returns a list of tokens."""
        tokens = []
        token_specification = [

            #('SPECIAL_CHAR', r'[\(\)]'),  # Special characters ( and )
            ('OPERATOR', r'APPLY_FILTER|APPLY_TRANSFORM|APPLY_ENHANCE'), # Operators
            ('KEYWORDS', r'START_OP|END_OP|START|END|TO_IMAGE|TO_FOLDER|sepia|negative|black_white|dark|red|green|blue|blur_gaussian|blur|contour|detail|edge|find_edges|smooth|sharpen|grayscale|emboss|brightness|contrast|color_enhance|definition|flip_horizontally|flip_vertically|rotate|crop'),  # All-keywords
            ('SKIP', r'[ \t]+'),         # Skip over spaces and tabs
            ('URL', r'\(.*?\)'),  # URL for file explorer paths in parentheses
            ('NUMBER', r'-?\d+(\.\d+)?'),  # Integer or decimal number, positive or negative
            ('MISMATCH', r'.'),          # Any other character
        ]

        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        print(tok_regex)
        for mo in re.finditer(tok_regex, code):
            print(mo)
            kind = mo.lastgroup
            value = mo.group()

            if kind == 'MISMATCH':
                # throws an error if the character is not recognized
                raise RuntimeError(f'Designer tools: {value!r} unexpected')
            if kind == 'SKIP':
                # ignores spaces and tabs
                continue
            # if all validations are fine, just add as a new token
            tokens.append(Token(kind, value))

        return tokens