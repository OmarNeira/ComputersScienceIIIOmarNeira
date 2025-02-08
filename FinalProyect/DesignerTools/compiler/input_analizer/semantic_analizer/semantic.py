class SemanticAnalyzer:
    """This class represents the behavior of a semantic analyzer."""

    def __init__(self, tokens_input: list):
        self.tokens = tokens_input
        self.operations = []
    
    def def_operations(self):
        """This method defines the operations."""
        n_operation = -1
        in_operation = False
        for token in self.tokens:
            print(token)
            if token.value == 'START_OP': #Every time a START_OP token is found, a new operation is started
                n_operation += 1
                self.operations.append([])  # Start a new operation list
                in_operation = True
            elif token.value == 'END_OP': #Every time an END_OP token is found, the operation is finished
                in_operation = False
            elif in_operation: #If the token is not START_OP or END_OP, it is added to the current operation
                self.operations[n_operation].append(token)  # Add token to the current operation

    def analyze(self):
        """This method analyzes the tokens and returns the notes."""
        print("Semantic analyzer")
        self.def_operations()  # Separate operations

        print(self.operations)
        
        return self.operations