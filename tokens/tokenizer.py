class Token():
    INTEGRAL_LITERAL = "INTEGRAL_LITERAL"
    LEFT_CURLY_B = "LEFT_CURLY_B"
    SINGLE_COMMENT = "SINGLE_COMMENT"
    INT = "INT"
    ASSIGN_OPERATOR = "ASSIGN_OPERATOR"
    ID = "ID"
    RIGHT_ROUND_B = "RIGHT_ROUND_B"
    SEMICOLON = "SEMICOLON"
    ELSE = "ELSE"
    GREAT_EQ = "GREAT_EQ"
    IF = "IF"
    ASTERISK = "ASTERICK"
    PLUS = "PLUS"
    GREATERTHAN = "GREATERTHAN"
    LEFT_ROUND_B = "LEFT_ROUND_B"
    RIGHT_CURLY_B = "RIGHT_CURLY_B"
    FOR = "FOR"
    RETURN = "RETURN"
    BREAK = "BREAK"
    def __init__(self, name, value):
        super().__init__()
        self.name = name
        self.value = value

class TokensRepo():

    __instance = None
    __queue = []

    @staticmethod
    def getInstance():
        """ static access method """
        if TokensRepo.__instance == None:
            TokensRepo()
        return TokensRepo.__instance

    def __init__(self):
        """ virtually private constructor  """
        super().__init__()
        if TokensRepo.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            TokensRepo.__instance = self

    def getQueue(self):
        """ return list of Token objects """
        return TokensRepo.__queue

    def addToken(self, token):
        """ add a token Obj """
        if isinstance(token, Token):
            TokensRepo.__queue.append(token)
        else:
            raise Exception("this method take Token obj")

    def hasNext(self):
        """ return flase if the queue is empty otherwise return true """
        if len(TokensRepo.__queue) > 0:
            return True
        else:
            return False

    def getNext(self):
        """ return the first Token Obj in the Queue """
        if self.hasNext():
            return TokensRepo.__queue[0]
        else:
            raise Exception("The Queue is Empty")

    def consume(self):
        """ return the first Token Obj in the Queue and delete it """
        if self.hasNext():
            token = TokensRepo.__queue.pop(0)
            return token
        else:
            raise Exception("The Queue is Empty")

    def isEmpty(self):
        return not self.hasNext()

