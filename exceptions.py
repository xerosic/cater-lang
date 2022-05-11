
class VmException(Exception):
    pass


class ParserException(Exception):
    pass


class IllegalInstuction(ParserException):
    pass


class NotEnoughParameters(ParserException):
    pass
