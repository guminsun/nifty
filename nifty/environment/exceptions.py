class SemanticError(Exception):
    '''Exception raised for semantical errors.

    Attributes:
        msg -- explanation of the error
    '''
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

def semantic_error(msg, node):
    try:
        line = node['line_number']
    # Catch nodes which doesn't have the key 'line_number' defined.
    except KeyError:
        line = None
    # Catch None. E.g. in case of undefined identifier.
    except TypeError:
        line = None
    msg = ('--- Semantic error on line %s, %s' % (line, msg))
    raise SemanticError(msg)

class SyntaxError(Exception):
    '''Exception raised for syntax errors.

    Attributes:
        msg -- explanation of the error
    '''
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return repr(self.msg)
