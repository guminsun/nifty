class NiftyError(Exception):
    '''Exception raised for nifty errors.

    Attributes:
        msg -- explanation of the error
    '''
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return repr(self.msg)

class LexicalError(NiftyError):
    '''Exception raised for lexical errors.

    Attributes:
        msg -- explanation of the error
    '''
    pass

def lexical_error(token):
    msg = ('--- Lexical error on line %d, illegal character \'%s\''
           % (token.lineno, token.value[0]))
    raise LexicalError(msg)

class SemanticError(NiftyError):
    '''Exception raised for semantical errors.

    Attributes:
        msg -- explanation of the error
    '''
    pass

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

class SyntaxError(NiftyError):
    '''Exception raised for syntax errors.

    Attributes:
        msg -- explanation of the error
    '''
    pass

def syntax_error(line_number, token):
    if line_number is not None:
        msg = ('--- Syntax error on line %d, unexpected token: \'%s\''
               % (line_number, token))
    else:
        msg = ('--- Syntax error, unexpected token: \'%s\'' % (token))
    raise SyntaxError(msg)
